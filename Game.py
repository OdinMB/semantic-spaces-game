import streamlit as st
import numpy as np
import json
import random
from scipy.spatial.distance import cdist
from visualization import visualize_embeddings, visualize_target_circle
from config import get_file_name
from template import prepare_page
from create_embeddings_openai import generate_npy
# from modify_index_html import check_index_html

file_name = get_file_name()
# Load the embeddings dictionary
embeddings_dict = np.load(f"{file_name}.npy", allow_pickle=True).item()

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

def choose_riddle(riddles_data):
    # First, filter out riddles that have been attempted
    unattempted_riddles = [r for r in riddles_data if r['id'] not in st.session_state.attempted_riddles]
    
    if file_name == "riddles_wip":
        filtered_riddles = unattempted_riddles
    else:
        # The first two riddles are a tutorial
        if len(st.session_state.attempted_riddles) < 2:
            filtered_riddles = [r for r in unattempted_riddles if 'intro' in r['tags']]
        # Later riddles are filtered based on the user's preferences
        else:
            selected_tags = [tag for tag, checked in [('weird', st.session_state.filter_weird), 
                                                    ('bias', st.session_state.filter_bias), 
                                                    ('satirical', st.session_state.filter_satirical)] if checked]
            filtered_riddles = [r for r in unattempted_riddles if any(tag in r['tags'] for tag in selected_tags)]

    if filtered_riddles:
        chosen_riddle = random.choice(filtered_riddles)
        st.session_state.riddle = chosen_riddle
        st.session_state.choice = False
        st.rerun()
    else:
        if st.session_state.reset_warning:
            st.session_state.reset_warning = False
            st.session_state.attempted_riddles = []
            reset_aiscore()
            choose_riddle(riddles_data)
        else:
            st.warning("You've attempted all available puzzles with the current filters. Click 'Next puzzle' to reset and try again.")
            st.session_state.reset_warning = True
    

def display_riddle(keywords):
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
    if 'reset_warning' not in st.session_state:
        st.session_state.reset_warning = False
    if 'aiscore_relalignment' not in st.session_state:
        st.session_state.aiscore_relalignment = 0
        st.session_state.aiscore_n = 0

    with open(f"{file_name}.json", 'r') as file:
        # Load the entire JSON data
        json_data = json.load(file)
        riddles_data = json_data['riddles']

    if 'riddle' not in st.session_state:
        choose_riddle(riddles_data)
    keywords = st.session_state.riddle["keywords"]
    options = st.session_state.riddle["options"]

    st.markdown("<h1 class='hide-on-mobile centered'>Semantic Spaces</h1>", unsafe_allow_html=True)

    if st.session_state.choice:
        if st.button("Next puzzle", type="primary"):
            choose_riddle(riddles_data)

    if not st.session_state.reset_warning:
        display_riddle(keywords)

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
                        st.markdown(f"**{term} (distance: {dist:.2f})** :star:")  # Highlight player's choice
                    else:
                        st.markdown(f"{term} (distance: {dist:.2f})")


if __name__ == '__main__':
    app()
