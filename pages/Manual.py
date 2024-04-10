import streamlit as st
from template import hide_menus

st.set_page_config(
    page_title="Semantic Spaces - Manual",
    page_icon="🤯",
)
hide_menus()

left_co, cent_co,last_co = st.columns([1, 3, 1])
with cent_co:
    st.image("img/labyrinth.jpg", width=400)
    st.markdown("<h1 style='text-align: center'>Semantic Spaces</h1>", unsafe_allow_html=True)

st.markdown("""\
Semantic distance measures how closely related two words are in meaning — like how 'coffee' naturally pairs with 'morning', or 'stars' with 'night'.
There's also direction. Which in the case of meaning can go through a lot of different dimensions. For instance, we can think of the semantic path from 'baron' to 'king' as moving through a nobility dimension, and that from 'water' to 'ice' as moving through a temperature and state-of-matter dimension.
This game asks you to follow these semantic pathways not as you intuitively understand them as a human, but as they are encoded in AI language models.
Can you trace a semantic path like an AI language model? Let's find out!

### Technical introduction
            
If you want to learn more about how AI language models construct semantic pathways, watch the 5-minute section of this video by Grant Sanderson (@3blue1brown) starting at 12m30s:
""")
st.video("https://www.youtube.com/watch?v=wjZofJX0v4M&t=802s")

