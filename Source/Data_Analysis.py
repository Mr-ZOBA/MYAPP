import streamlit as st

from Code.DA.Streaming import stream
from Code.DA.Uber import uber


def DataAnalysis():
    # ---------------- Menu-----------------
    menu1 = ['Uber', 'Streaming', 'New_project']
    choice = st.sidebar.selectbox('DataBase', menu1)

    if choice == "Streaming":
        stream()
    if choice == "Uber":
        uber()

DataAnalysis()