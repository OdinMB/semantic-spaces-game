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
<p style='font-size: 20px;'>Semantic distance measures how closely related two words are in meaning — like how <span style='background-color: #FFFF00; padding: 0 3px; margin: 0 3px; color: #000'>coffee</span> naturally pairs with <span style='background-color: #FFFF00; padding: 0 3px; margin: 0 3px; color: #000'>morning</span>, or <span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>stars</span> with <span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>night</span>.</p>

<p style='font-size: 20px;'>There's also direction. Which in the case of meaning can go through a lot of different dimensions. 
For instance, we can think of the semantic path from <span style='background-color: #FFFF00; padding: 0 3px; margin: 0 3px; color: #000'>baron</span> to <span style='background-color: #FFFF00; padding: 0 3px; margin: 0 3px; color: #000'>king</span> as moving through a nobility dimension, and that from <span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>water</span> to <span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>ice</span> as moving through a temperature and state-of-matter dimension.</p>
            
<p style='font-size: 20px;'>This game asks you to follow these semantic pathways not as you intuitively understand them as a human, but as they are encoded in AI language models. Click <a href="http://localhost:8501/Learn_about_AI" target="_self">here</a> to learn more about how AI language models construct semantic pathways.</p>

<p style='font-size: 20px;'>Here's an example. Imagine the semantic path from <span style='background-color: #FFFF00; padding: 0 3px; margin: 0 3px; color: #000'>water</span> to <span style='background-color: #FFFF00; padding: 0 3px; margin: 0 3px; color: #000'>ice</span>. Now follow the same path but with <span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>Austrians</span> as the starting point. Where do you land? What's a colder and more solidified version of Austrians (plus whatever other semantic shifts happen from water to ice)? According to the AI, it's <span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>Germans</span>!</p>

<p style='font-size: 20px;'>Before you get too excited: <span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>Germans</span> is not exactly where you arrive after applying the path from <span style='background-color: #FFFF00; padding: 0 3px; margin: 0 3px; color: #000'>water</span> to <span style='background-color: #FFFF00; padding: 0 3px; margin: 0 3px; color: #000'>ice</span> to <span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>Austrians</span>. It is just the semantically closest out of the six options that the game offers you for this puzzle.</p>

<p style='font-size: 20px;'>Can you trace a semantic path like an AI language model? Let's find out!</p>
""", unsafe_allow_html=True)