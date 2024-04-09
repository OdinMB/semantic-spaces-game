import streamlit as st
import numpy as np
import random
from scipy.spatial.distance import cdist
from visualization import visualize_embeddings, visualize_target_circle
from config import file_name

# Load the embeddings dictionary
embeddings_dict = np.load(f"{file_name}.npy", allow_pickle=True).item()

def get_embedding(term):
    embedding = embeddings_dict.get(term.strip(), None)
    if embedding is not None:
        return np.array(embedding)
    else:
        return np.zeros((1536,))

def calculate_distance(target_vector, option_embedding):
    return cdist(target_vector.reshape(1, -1), option_embedding.reshape(1, -1), 'cosine')[0][0]

def app():
    st.title("Semantic Spaces")
    expander = st.expander("How does this work?")
    expander.write("""\
        Semantic distance measures how closely related two words are in meaning — like how 'coffee' naturally pairs with 'morning', or 'stars' with 'night'.
        But there's more: semantic direction navigates the nuanced paths between words. For instance, 'bark' moves in one direction to align with 'tree', and in another, entirely different direction towards 'dog'.
        This game delves into these intricate connections — not as mapped by human intuition but as charted by AI language models.
        As you explore, remember: the AI's interpretation of semantic relationships can often surprise or seem alien to us.
        Can you trace a semantic path like an AI language model? Let's find out!
    """)

    if 'attempted_riddles' not in st.session_state:
        st.session_state.attempted_riddles = []

    with open(f"{file_name}.txt", "r") as file:
        riddles_data = [line.strip().split(';') for line in file.readlines()]

    if st.button("New puzzle") or 'riddle_data' not in st.session_state:
        # Filter riddles that haven't been attempted
        unattempted_riddles = [r for i, r in enumerate(riddles_data) if i not in st.session_state.attempted_riddles]
        
        # Check if there are any unattempted riddles left
        if unattempted_riddles:
            # Randomly select from unattempted riddles
            chosen_riddle = random.choice(unattempted_riddles)
            chosen_index = riddles_data.index(chosen_riddle)
            
            # Update session state with chosen riddle
            st.session_state.riddle_data = chosen_riddle
            st.session_state.riddle = chosen_riddle[:3]
            st.session_state.options = chosen_riddle[3:]
            st.session_state.choice_made = False
            
            # Record this riddle as attempted
            st.session_state.attempted_riddles.append(chosen_index)
        else:
            st.warning("You've attempted all available puzzles! Resetting...")
            st.session_state.attempted_riddles = []  # Reset attempted riddles

    word1, word2, word3 = st.session_state.riddle
    options = st.session_state.options

    st.markdown(f"""
    <div style='font-size: 20px; margin-top: 10px; margin-bottom: 30px'>
        The semantic distance between <span style='background-color: #FFFF00; padding: 0 3px; margin: 0 3px; color: #000'>{word1}</span> and 
        <span style='background-color: #FFFF00; padding: 0 3px; margin: 0 3px; color: #000'>{word2}</span> is similar to<BR />
        the semantic distance between <span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>{word3}</span> and 
        <span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>_____</span> ?
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 20px;  # Optional: Adjusts the button's border-radius
    }
    </style>""", unsafe_allow_html=True)

    if not st.session_state.get('choice_made', False):
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
                            st.session_state['choice_made'] = True
                            st.rerun()


    if st.session_state.choice_made:
        target_vector = get_embedding(word3) + get_embedding(word2) - get_embedding(word1)
        distances = [(option, calculate_distance(target_vector, get_embedding(option))) for option in options]
        sorted_options = sorted(distances, key=lambda x: x[1])

        # Display the sorted options
        # st.markdown("### Result")
        # for term, dist in sorted_options:
        #     if term == st.session_state.choice:
        #         st.markdown(f"**{term} (distance: {dist:.2f})** :star:")  # Highlight player's choice
        #     else:
        #         st.markdown(f"{term} (distance: {dist:.2f})")

        # After calculating distances and sorting options
        fig_target_circle = visualize_target_circle(sorted_options, st.session_state.choice)
        st.pyplot(fig_target_circle)

        # Embeddings visualization in 2D map
        # fig = visualize_embeddings(get_embedding, [word1, word2, word3], options, st.session_state.choice, target_vector, 2)
        # st.pyplot(fig)

if __name__ == '__main__':
    app()