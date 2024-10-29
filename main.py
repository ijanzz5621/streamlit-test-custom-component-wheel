import streamlit as st
from discrete_slider import discrete_slider

sel_val = discrete_slider(["test1", "test2", "test3", "test4", "test5"])
st.write("You have selected: ", sel_val)
