import streamlit as st

def prepare_page():
    st.markdown("""
        <style>
            .block-container {
                margin-top: -4em;
            }
            #MainMenu {visibility: hidden;}
            .stDeployButton {display:none;}
            footer {visibility: hidden;}
            #stDecoration {display:none;}

            .stButton>button {
                width: 100%;
                border-radius: 20px;  # Optional: Adjusts the button's border-radius
            }
        </style>
    """, unsafe_allow_html=True)