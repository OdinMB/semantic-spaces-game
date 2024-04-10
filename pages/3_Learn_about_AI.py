import streamlit as st
from template import prepare_page

st.set_page_config(
    page_title="Semantic Spaces - Learn about AI",
    page_icon="🤯",
)
prepare_page()

left_co, cent_co,last_co = st.columns([1, 3, 1])
with cent_co:
    st.image("img/labyrinth.jpg")
    st.markdown("<h1 style='text-align: center'>Learn about AI</h1>", unsafe_allow_html=True)

st.markdown("""\
<p style='font-size: 20px;'>If you want to learn more about how AI language models construct semantic pathways, watch this video by Grant Sanderson (@3blue1brown). Jump to 12m30s and watch for 6 minutes:</p>
""", unsafe_allow_html=True)
st.video("https://www.youtube.com/watch?v=wjZofJX0v4M&t=802s")

left_co, cent_co,last_co = st.columns([1, 3, 1])
with cent_co:
    st.markdown("<h1 style='text-align: center'>Disclaimer</h1>", unsafe_allow_html=True)

st.markdown(f"""\
<p style='font-size: 20px;'>This game claims that <span style='background-color: #FFFF00; padding: 0 3px; margin: 0 3px; color: #000'>bee</span> is to 
<span style='background-color: #FFFF00; padding: 0 3px; margin: 0 3px; color: #000'>cockroach</span> as 
<span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>teacher</span> is to
<span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>lobbyist</span>.
</p>                    
<p style='font-size: 20px;'>
It also claims that <span style='background-color: #FFFF00; padding: 0 3px; margin: 0 3px; color: #000'>water</span> is to 
<span style='background-color: #FFFF00; padding: 0 3px; margin: 0 3px; color: #000'>ice</span> as 
<span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>Austrians</span> is to
<span style='background-color: #DDDD00; padding: 0 3px; margin: 0 3px; color: #000'>Germans</span>.
</p>

<p style='font-size: 20px;'>If you watched the video, you'll know that these are not my personal opinions. They are absolutely objective assessments by a state-of-the-art AI language model. 😉 Please send any complaints to OpenAI.</p>
""", unsafe_allow_html=True)
