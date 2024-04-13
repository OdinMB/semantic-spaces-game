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
                
            .fa {
                padding: 6px;
                font-size: 20px;
                width: 32px;
                height: 32px;
                text-align: center;
                text-decoration: none;
            }
            .fa:hover {
                opacity: 0.7;
                text-decoration: none;
            }
            .fa-facebook {
                background: #3B5998;
            }
            .fa-twitter {
                background: #55ACEE;
            }
            .fa-google {
                background: #dd4b39;
            }
            .fa-linkedin {
                background: #007bb5;
            }
            .fa-instagram {
                background: #125688;
            }
            .fa-pinterest {
                background: #cb2027;
            }
            .fa-snapchat-ghost {
                background: #fffc00;
                text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;
            }
            .fa-whatsapp {
                background: #25d366;
            }
        </style>
    """, unsafe_allow_html=True)

    # https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_social_media_buttons
    # <a href="https://plus.google.com/share?url=https%3A%2F%2Fsemantics.fun" class="fa fa-google" style="color: white"></a>
    # <a href="#" class="fa fa-snapchat-ghost" style="color: white"></a>
    st.sidebar.markdown("""
        <div class="centered" style="margin-top: 20px; margin-bottom: 35px">
        <a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fsemantics.fun" class="fa fa-facebook" style="color: white"></a>
        <a href="https://twitter.com/intent/tweet?url=https%3A%2F%2Fsemantics.fun&amp;text=Semantic%20Spaces%3A%20A%20puzzle%20game%20about%20language%20and%20AI.%20Is%20%22civilization%20in%20decline%22%20semantically%20closer%20to%20%22social%20media%20influencers%22%20or%20%22fast%20food%20empires%22%3F%20Guess%20how%20a%20powerful%20AI%20model%20would%20answer%20this%20and%20many%20other%20serious%20questions.%0A%23ai%20%23semantics%20%23fun   " class="fa fa-twitter" style="color: white"></a>
        <a href="https://www.linkedin.com/shareArticle?mini=true&amp;url=https%3A%2F%2Fsemantics.fun&amp;title=Semantic%20Spaces&amp;summary=A%20puzzle%20game%20about%20language%20and%20AI.%20Is%20%22civilization%20in%20decline%22%20semantically%20closer%20to%20%22social%20media%20influencers%22%20or%20%22fast%20food%20empires%22%3F%20Guess%20how%20a%20powerful%20AI%20model%20would%20answer%20this%20and%20many%20other%20serious%20questions.%0A%23ai%20%23semantics%20%23fun&amp;source=" class="fa fa-linkedin" style="color: white"></a>
        <a href="https://www.instagram.com/?url=http%3A%2F%2Fsemantics.fun" class="fa fa-instagram" style="color: white"></a>
        <a href="https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fsemantics.fun&amp;media=https%3A%2F%2Fsemantics.fun%2Fmedia%2Fb7a257bff0148d91976885bc9324c8bb78c806f1a83a608ccbe01a30.jpg&amp;description=Semantic%20Spaces%3A%20A%20puzzle%20game%20about%20language%20and%20AI.%20Is%20%22civilization%20in%20decline%22%20semantically%20closer%20to%20%22social%20media%20influencers%22%20or%20%22fast%20food%20empires%22%3F%20Guess%20how%20a%20powerful%20AI%20model%20would%20answer%20this%20and%20many%20other%20serious%20questions.%0A%23ai%20%23semantics%20%23fun" class="fa fa-pinterest" style="color: white"></a>
        <a href="https://api.whatsapp.com/send?text=Semantic Spaces - A game about language and AI%0a%0aIs 'civilization in decline' semantically closer to 'social media influencers' or 'fast food empires'? Compare your intuition to a modern AI language model.%0a%0ahttp://semantics.fun" class="fa fa-whatsapp" style="color: white"></a>
        </div>
    """, unsafe_allow_html=True)

    st.sidebar.info("No tracking, no ads.")
    st.sidebar.info("'Semantic Spaces' by Odin Mühlenbein is published under a [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).")
    st.sidebar.info("""Want to improve the game? Add puzzles? Visit [GitHub](https://github.com/OdinMB/semantic-spaces-game).""")
