import streamlit as st
from template import prepare_page

st.set_page_config(
    page_title="Semantic Spaces - How to play",
    page_icon="🤯",
)
prepare_page()

left_co, cent_co,last_co = st.columns([1, 3, 1])
with cent_co:
    # st.image("img/labyrinth.jpg")
    st.markdown("<h1 style='text-align: center'>How to play</h1>", unsafe_allow_html=True)

st.markdown("""\

<p style='font-size: 20px;'>Use your intuition and compare it to that of a <a href="/Learn_about_AI" target="_self">modern AI language model</a>.</p>

<hr>
            
<p style='font-size: 20px;'><span style='background-color: #EEEE00; padding: 0 3px; margin: 0 3px; color: #000'>Stars</span> 
        is closest to <span style='background-color: #EEEE00; padding: 0 40px; margin: 0 3px; color: #000'>?</span>.</p>
                        
<p style='font-size: 20px;'>This is a puzzle about semantic distance, or how closely related two terms are in meaning. <span style='background-color: #EEEE00; padding: 0 3px; margin: 0 3px; color: #000'>Stars</span> naturally pairs with <span style='background-color: #EEEE00; padding: 0 3px; margin: 0 3px; color: #000'>moon</span> (because the two are often seen together) and <span style='background-color: #EEEE00; padding: 0 3px; margin: 0 3px; color: #000'>sun</span> (because the sun is a star). It's a bit further away from <span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>universe</span>.</p>

<hr>            

<p style='font-size: 20px;'>
            <span style='background-color: #EEEE00; padding: 0 3px; margin: 0 3px; color: #000'>Water</span> is to 
            <span style='background-color: #EEEE00; padding: 0 3px; margin: 0 3px; color: #000'>ice</span> <span style='margin-left: 15px; margin-right: 15px;'>as</span>
            <span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>Austrians</span> is to 
            <span style='background-color: #DDDD00; padding: 0 40px; margin: 0 3px; color: #000'>?</span>.</p>
            
<p style='font-size: 20px;'>This is a puzzle about semantic pathways. Pathways often go through several dimensions.
The path from <span style='background-color: #EEEE00; padding: 0 3px; margin: 0 3px; color: #000'>water</span> to <span style='background-color: #EEEE00; padding: 0 3px; margin: 0 3px; color: #000'>ice</span> moves through a temperature and a state-of-matter dimension. What's a colder and more solidified version of <span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>Austrians</span> (plus whatever other semantic shifts you think are happening from water to ice)? The AI thinks that the closest option is <span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>Germans</span>!</p>
""", unsafe_allow_html=True)

if st.button("Play", type="primary"):
    st.switch_page("Game.py")

# <p style='font-size: 20px;'>Before you get too excited: <span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>Germans</span> is not exactly where you arrive after applying the path from <span style='background-color: #EEEE00; padding: 0 3px; margin: 0 3px; color: #000'>water</span> to <span style='background-color: #EEEE00; padding: 0 3px; margin: 0 3px; color: #000'>ice</span> to <span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>Austrians</span>. It is just the semantically closest out of the six options that the game offers you for this puzzle.</p>
# <p style='font-size: 20px;'>Similarly for semantic distances. Out of the six options, <span style='background-color: #EEEE00; padding: 0 3px; margin: 0 3px; color: #000'>a man's job</span> is closest to <span style='background-color: #EEEE00; padding: 0 3px; margin: 0 3px; color: #000'>lawyer</span>, while <span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>a woman's job</span> is closest to <span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>nurse</span>. (That's called bias.)
# <p style='font-size: 20px;'>Can you estimate semantic distances and trace semantic paths like an AI language model? Let's find out!</p>