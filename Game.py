import streamlit as st
import numpy as np
import json
import random
from scipy.spatial.distance import cdist
from visualization import visualize_embeddings, visualize_target_circle
from config import get_file_name
from template import prepare_page
from tags import get_tag_data
from groups import get_group_data
from create_embeddings_openai import generate_npy
# from modify_index_html import check_index_html

file_name = get_file_name()
# Load the embeddings dictionary
embeddings_dict = np.load(f"{file_name}.npy", allow_pickle=True).item()

group_data = get_group_data()

def get_embedding(term):
    term = term.strip()
    if term == "":
        return np.zeros((1536,))

    global embeddings_dict  
    embedding = embeddings_dict.get(term, None)
    if embedding is None:
        # Generate the embedding and save it to the dictionary
        generate_npy(file_name)
        embeddings_dict = np.load(f"{file_name}.npy", allow_pickle=True).item()
        embedding = embeddings_dict.get(term, None)
        if embedding is None:
            # If the term is still not in the dictionary, return a zero vector
            return np.zeros((1536,))
    return np.array(embedding)

def calculate_distance(target_vector, option_embedding):
    return cdist(target_vector.reshape(1, -1), option_embedding.reshape(1, -1), 'cosine')[0][0]

def complete_active_group():
    remaining_riddles = set(group_data[st.session_state.active_group]["riddles"]) - set(st.session_state.attempted_riddles)
    st.session_state.excluded_riddles.extend(list(remaining_riddles))
    st.session_state.active_group = None
    st.session_state.group_sequence = 0


def choose_riddle(riddles_data):
    # First, filter out riddles that have been attempted or excluded
    unattempted_riddles = [r for r in riddles_data if r['id'] not in st.session_state.attempted_riddles and r['id'] not in st.session_state.excluded_riddles]

    filtered_riddles = None

    # Check 1: riddle creation mode
    if file_name == "riddles_wip":
        filtered_riddles = unattempted_riddles

    # Check 2: active group to continue
    if not filtered_riddles and st.session_state.active_group:
        sequence_to_continue = group_data[st.session_state.active_group].get("sequence", False) and st.session_state.group_sequence < group_data[st.session_state.active_group]["sequence"]
        unattempted_riddles_in_group = any(r['id'] in group_data[st.session_state.active_group]["riddles"] for r in unattempted_riddles)
        if sequence_to_continue and unattempted_riddles_in_group:
            filtered_riddles = [r for r in unattempted_riddles if r['id'] in group_data[st.session_state.active_group]["riddles"]]
        else:
            complete_active_group()

    # Check 3: tutorial mode
    if not filtered_riddles and len(st.session_state.attempted_riddles) < 2:
        filtered_riddles = [r for r in unattempted_riddles if 'intro' in r['tags']]
    
    # Default: select based on tags
    if not filtered_riddles:
        selected_tags = [tag for tag, checked in [('weird', st.session_state.filter_weird), 
                                                ('bias', st.session_state.filter_bias), 
                                                ('satirical', st.session_state.filter_satirical)] if checked]
        filtered_riddles = [r for r in unattempted_riddles if any(tag in r['tags'] for tag in selected_tags)]

    # If there are riddles to show, select one at random
    if filtered_riddles:
        chosen_riddle = random.choice(filtered_riddles)
        st.session_state.riddle = chosen_riddle
        st.session_state.choice = False
        
        # Activate the group if the chosen riddle belongs to one
        if 'group' in chosen_riddle:
            st.session_state.active_group = chosen_riddle['group']
            st.session_state.group_sequence += 1
        
        st.rerun()
    # If there are no riddles left, show a message and reset the game
    else:
        if st.session_state.reset_warning:
            reset_game()
            choose_riddle(riddles_data)
        else:
            st.success("You've played all available puzzles with the current filters. Click 'Next puzzle' to reset and try again.")
            st.link_button("Give feedback", url="https://z3y0hxrh.forms.app/semantic-spaces", type="primary", use_container_width=True)
            # st.info("""
            #     If you have any feedback or suggestions, please let us know by filling out the 
            #     [feedback form](https://z3y0hxrh.forms.app/semantic-spaces).
            # """)
            st.session_state.reset_warning = True

def display_labels(tags=[], group=""):
    if tags or group:
        tags_data = get_tag_data()
        # Use a container to hold all labels
        with st.container():
            # Create a raw HTML string for tags
            # This uses flexbox for layout, allowing tags to wrap as needed
            tags_html = "".join([
                f"""<div style="margin-right: 2px; text-align: center; background-color: #F0F2F6; padding: 2px 10px; display: inline-flex; align-items: center; justify-content: center; color: #555; font-size: 12px;">{tags_data[tag]["display"]}</div>"""
                for tag in tags
            ])
            if group:
                group_data = get_group_data()
                group_label = group_data[group]["label"]
                tags_html += f"""<div style="margin-right: 2px; text-align: center; background-color: #F0F2F6; padding: 2px 10px; display: inline-flex; align-items: center; justify-content: center; color: #555; font-size: 12px;">{group_label}</div>"""
            # Use column to display the tags HTML. The unsafe_allow_html=True allows HTML content.
            # The use of .markdown here is a workaround to allow custom HTML content in Streamlit.
            st.markdown(f"<div style='display: flex; flex-wrap: wrap; gap: 5px;'>{tags_html}</div>", unsafe_allow_html=True)

def display_riddle(keywords, tags=[]):
    # Semantic path riddle
    if len(keywords) == 3:
        word1, word2, word3 = keywords
        word1 = word1[0].upper() + word1[1:]
        st.markdown(f"""
        <div style='font-size: 20px; margin-top: 10px; margin-bottom: 30px'>
            <span style='background-color: #EEEE00; padding: 0 3px; margin: 0 3px 0 0; color: #000'>{word1}</span> is to 
            <span style='background-color: #EEEE00; padding: 0 3px; margin: 0 3px; color: #000'>{word2}</span> <span style='margin-left: 15px; margin-right: 15px;'>as</span>
            <span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>{word3}</span> is to 
            <span style='background-color: #DDDD00; padding: 0 40px; margin: 0 3px; color: #000;'>?</span>.
        </div>
        """, unsafe_allow_html=True)
        # <span class="hide-on-mobile"><br /></span>
    # Semantic distance riddle
    else:
        keyword = keywords[0]
        keyword = keyword[0].upper() + keyword[1:]
        st.markdown(f"""
        <div style='font-size: 20px; margin-top: 10px; margin-bottom: 30px'><span style='background-color: #EEEE00; padding: 0 3px 0 0; margin: 0 3px; color: #000'>{keyword}</span> 
        is closest to <span style='background-color: #EEEE00; padding: 0 40px; margin: 0 3px; color: #000'>?</span>.
        </div>
        """, unsafe_allow_html=True)

def display_options(options):
    # Determine the total number of rows needed
    total_options = len(options)
    rows_needed = (total_options + 2) // 3  # +2 for rounding up in integer division

    for row in range(rows_needed):
        # Each row will have up to three columns for buttons
        cols = st.columns(3)
        
        for i in range(3):
            option_index = row * 3 + i
            if option_index < total_options:  # Check to not exceed the list index
                option = options[option_index]
                with cols[i]:  # Place the button in the ith column of the current row
                    button_key = f"option_{option_index}"  # Unique key for each button
                    if st.button(option, key=button_key):
                        st.session_state['choice'] = option
                        # Record this riddle as attempted by its 'id'
                        st.session_state.attempted_riddles.append(st.session_state.riddle['id'])
                        st.rerun()

def reset_game():
    st.session_state.reset_warning = False
    st.session_state.attempted_riddles = []
    st.session_state.active_group = None
    st.session_state.group_sequence = 0
    st.session_state.excluded_riddles = []
    reset_aiscore()

def reset_aiscore():
    st.session_state.aiscore_relalignment = 0
    st.session_state.aiscore_n = 0

def adjust_ai_score(sorted_options, target_vector, player_choice):
    closest_dist = sorted_options[0][1]
    furthest_dist = sorted_options[-1][1]
    choice_dist = calculate_distance(target_vector, get_embedding(player_choice))
    rel_alignment = 1 - (choice_dist - closest_dist) / (furthest_dist - closest_dist)
    st.session_state.aiscore_relalignment += rel_alignment
    st.session_state.aiscore_n += 1

def app():
    st.set_page_config(
        page_title="Semantic Spaces",
        page_icon="🤯",
        layout="wide"
    )
    prepare_page()

    # Ensure session states are available
    if 'attempted_riddles' not in st.session_state:
        st.session_state.attempted_riddles = []
    if 'active_group' not in st.session_state:
        st.session_state.active_group = None
    if 'group_sequence' not in st.session_state:
        st.session_state.group_sequence = 0
    if 'excluded_riddles' not in st.session_state:
        st.session_state.excluded_riddles = []
    if 'reset_warning' not in st.session_state:
        st.session_state.reset_warning = False
    if 'aiscore_relalignment' not in st.session_state:
        st.session_state.aiscore_relalignment = 0
        st.session_state.aiscore_n = 0

    with open(f"{file_name}.json", 'r') as file:
        # Load the entire JSON data
        json_riddles_data = json.load(file)
        riddles_data = json_riddles_data['riddles']

    if 'riddle' not in st.session_state:
        choose_riddle(riddles_data)
    keywords = st.session_state.riddle["keywords"]
    options = st.session_state.riddle["options"]
    tags = st.session_state.riddle["tags"]
    group = st.session_state.riddle.get("group", None)

    st.markdown("<h1 class='hide-on-mobile centered'>Semantic Spaces</h1>", unsafe_allow_html=True)

    if st.session_state.choice:
        if st.button("Next puzzle", type="primary"):
            choose_riddle(riddles_data)

    # Display a note about choosing puzzle themes with the third puzzle
    if len(st.session_state.attempted_riddles) == 2 and not st.session_state.choice:
        st.info("Open the menu to choose which types of puzzles you get (top left)")

    # Exceptions: message for the player and selecting themes after the 2nd puzzle
    if not st.session_state.reset_warning:

        # don't show the theme tags on the results page
        if not st.session_state.choice:
            display_labels(tags, group)

        display_riddle(keywords, tags)

        if not st.session_state.get('choice', False):
            display_options(options)
            if len(st.session_state.attempted_riddles) < 2 and not st.session_state.choice:
                st.markdown(f"""<div class='centered' style='font-size: 20px; margin-top: 10px; margin-bottom: 10px'><a href="/How_to_play" target="_self">How does this work?</a></div>""", unsafe_allow_html=True)

        if st.session_state.get('choice', False):
            if len(keywords) == 3:
                target_vector = get_embedding(keywords[2]) + get_embedding(keywords[1]) - get_embedding(keywords[0])
            else:
                target_vector = get_embedding(keywords[0])
            distances = [(option, calculate_distance(target_vector, get_embedding(option))) for option in options]
            sorted_options = sorted(distances, key=lambda x: x[1])
            
            # Adjust the AI alignment score
            adjust_ai_score(sorted_options, target_vector, st.session_state.choice)

            # Show the AI response as a target cirlce
            visualize_target_circle(sorted_options, st.session_state.choice)

            # if st.button("Next puzzle"):
                # choose_riddle(riddles_data)

            # Embeddings visualization in 2D map
            # fig = visualize_embeddings(get_embedding, [word1, word2, word3], options, st.session_state.choice, target_vector, 2)
            # st.pyplot(fig)

            # Display the AI alignment score after the player has made a choice
            if st.session_state.aiscore_n > 0:
                ai_alignment_score = st.session_state.aiscore_relalignment / st.session_state.aiscore_n
                puzzle_text = "puzzles" if st.session_state.aiscore_n > 1 else "puzzle"
                st.markdown(f"<div class='centered' style='margin-top: -45px'>Your intuition is {round(ai_alignment_score*100)}% aligned with AI ({st.session_state.aiscore_n} {puzzle_text}).</div>", unsafe_allow_html=True)

            # If in riddle creation mode: display the options with cosine distances
            if file_name == "riddles_wip":
                st.markdown("### Result")
                for term, dist in sorted_options:
                    if term == st.session_state.choice:
                        st.markdown(f"**{term} (distance: {dist:.3f})** :star:")  # Highlight player's choice
                    else:
                        st.markdown(f"{term} (distance: {dist:.3f})")


if __name__ == '__main__':
    app()
