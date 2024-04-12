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

            [data-testid="stSidebar"][aria-expanded="true"]{
                min-width: 275px;
                max-width: 275px;
            }
                
            .stButton>button {
                width: 100%;
                border-radius: 20px;
            }
            @media screen and (max-width: 767px) {
                .hide-on-mobile {
                    display: none;
                }
            }
            .centered {
                text-align: center;
                width: 100%;
            }
        </style>
    """, unsafe_allow_html=True)

    st.sidebar.info("No cookies, no tracking, no ads. Just fun with language.")
    st.sidebar.info("'Semantic Spaces' by Odin Mühlenbein is published under a [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).")
    st.sidebar.info("""Want to improve the game? Add puzzles? Visit [GitHub](https://github.com/OdinMB/semantic-spaces-game).""")

