import streamlit as st
from template import prepare_page
import os
from dotenv import load_dotenv
load_dotenv()
import json
import pandas as pd

st.set_page_config(
    page_title="Semantic Spaces - Admin Area",
    page_icon="🤯",
)
prepare_page()

def display_riddles_table(riddles_data):
    # Convert the list of dictionaries into a DataFrame for easier display
    # Explicitly set the 'id' field as the index of the DataFrame
    df = pd.DataFrame(riddles_data).set_index('id')
    
    # Optional: Convert lists in 'keywords', 'options', and 'tags' columns to comma-separated strings for cleaner display
    for column in ['keywords', 'options', 'tags']:
        if column in df.columns:
            df[column] = df[column].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)
    
    # Display the DataFrame as a table in Streamlit
    st.table(df)



# Function to display the admin interface
def admin_interface():
    st.title("Puzzle Admin Page")

    with open("riddles.json", 'r') as file:
        # Load the entire JSON data
        json_data = json.load(file)
        riddles_data = json_data['riddles']

    display_riddles_table(riddles_data)


def main():
    # Check if a PASSWORD environment variable is set
    password_protected = "PASSWORD" in os.environ
    
    # If PASSWORD is set and the user hasn't been authenticated yet, show the login form
    if password_protected and not st.session_state.get('password_entered', False):
        with st.form("login_form", clear_on_submit=False):
            password = st.text_input("Enter the password:", type="password", key="password_field")
            submit_button = st.form_submit_button("Login")
            
            if submit_button:
                if password == os.environ['PASSWORD']:
                    st.session_state['password_entered'] = True  # Mark the user as authenticated
                    st.rerun();
                    st.success("Password correct. Welcome!")
                else:
                    st.error("Password incorrect. Please try again.")
                    
    # If the PASSWORD is not set or the user has been authenticated, show the admin interface
    if not password_protected or st.session_state.get('password_entered', False):
        admin_interface()

if __name__ == "__main__":
    main()

