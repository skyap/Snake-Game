import multiprocessing
import streamlit as st
from backend import *

st.title("Turtle App")
title = st.text_input("Canvas Title", value="My Canvas")
width = st.number_input("Canvas Width", value=500)
height = st.number_input("Canvas Height", value=500)
length = st.number_input("Square Length", value=200)
clicked = st.button("Paint")

t = multiprocessing.Process(target=canvas_builder, args=(title, width, height, length,))

if clicked:
   t.start()