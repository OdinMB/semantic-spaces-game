import streamlit as st
from template import prepare_page

st.set_page_config(
    page_title="Semantic Spaces - How to play",
    page_icon="🤯",
)
prepare_page()

left_co, cent_co,last_co = st.columns([1, 3, 1])
with cent_co:
    st.image("img/labyrinth.jpg")
    st.markdown("<h1 style='text-align: center'>How to play</h1>", unsafe_allow_html=True)

st.markdown("""\
<p style='font-size: 20px;'>Semantic distance measures how closely related two terms are in meaning — like how <span style='background-color: #EEEE00; padding: 0 3px; margin: 0 3px; color: #000'>coffee</span> naturally pairs with <span style='background-color: #EEEE00; padding: 0 3px; margin: 0 3px; color: #000'>morning</span>, or <span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>stars</span> with <span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>night</span>.</p>

<p style='font-size: 20px;'>There's also direction. Which in the case of meaning can go through a lot of different dimensions. 
For instance, we can think of the semantic path from <span style='background-color: #EEEE00; padding: 0 3px; margin: 0 3px; color: #000'>baron</span> to <span style='background-color: #EEEE00; padding: 0 3px; margin: 0 3px; color: #000'>king</span> as moving through a nobility dimension, and that from <span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>water</span> to <span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>ice</span> as moving through a temperature and state-of-matter dimension.</p>

<p style='font-size: 20px;'>Here's an example. Imagine the semantic path from <span style='background-color: #EEEE00; padding: 0 3px; margin: 0 3px; color: #000'>water</span> to <span style='background-color: #EEEE00; padding: 0 3px; margin: 0 3px; color: #000'>ice</span>. Now follow the same path but with <span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>Austrians</span> as the starting point. Where do you land? What's a colder and more solidified version of Austrians (plus whatever other semantic shifts you think are happening from water to ice)? Maybe <span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>Alps</span>? Or <span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>Germans</span>?</p>

<p style='font-size: 20px;'>Use your intuition and then compare your results with those of a <a href="/Learn_about_AI" target="_self">modern AI language model</a>.</p>
""", unsafe_allow_html=True)

# <p style='font-size: 20px;'>Before you get too excited: <span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>Germans</span> is not exactly where you arrive after applying the path from <span style='background-color: #EEEE00; padding: 0 3px; margin: 0 3px; color: #000'>water</span> to <span style='background-color: #EEEE00; padding: 0 3px; margin: 0 3px; color: #000'>ice</span> to <span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>Austrians</span>. It is just the semantically closest out of the six options that the game offers you for this puzzle.</p>
# <p style='font-size: 20px;'>Similarly for semantic distances. Out of the six options, <span style='background-color: #EEEE00; padding: 0 3px; margin: 0 3px; color: #000'>a man's job</span> is closest to <span style='background-color: #EEEE00; padding: 0 3px; margin: 0 3px; color: #000'>lawyer</span>, while <span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>a woman's job</span> is closest to <span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>nurse</span>. (That's called bias.)
# <p style='font-size: 20px;'>Can you estimate semantic distances and trace semantic paths like an AI language model? Let's find out!</p>