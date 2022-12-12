import streamlit as st

name = st.text_input("Name:")

st.write("Hello " + name)
st.write("How are you?")
