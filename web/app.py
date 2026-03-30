import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Strategic Geospatial Ecosystem",
    layout="wide"
)

with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

components.html(html_code, height=5000, scrolling=True)
