import streamlit as st
from template import prepare_page

st.set_page_config(
    page_title="Semantic Spaces - License + Contributions",
    page_icon="🤯",
)
prepare_page()

left_co, cent_co,last_co = st.columns([1, 3, 1])
with cent_co:
    st.image("img/labyrinth.jpg", width=400)
    st.markdown("<h1 style='text-align: center'>License</h1>", unsafe_allow_html=True)

st.markdown("""
    <p style='font-size: 20px;'>'Semantic Spaces' by Odin Mühlenbein is published under a CC-BY 4.0 license.</p>
""", unsafe_allow_html=True)

left_co, cent_co,last_co = st.columns([1, 3, 1])
with cent_co:
    st.markdown("<h1 style='text-align: center'>Contributions</h1>", unsafe_allow_html=True)

st.markdown("""\
    <p  style='font-size: 20px;'>Contributions are welcome! Please visit the <a href="https://github.com/OdinMB/semantic-spaces-game" target="_blank">GitHub</a> repository.</p>
""", unsafe_allow_html=True)