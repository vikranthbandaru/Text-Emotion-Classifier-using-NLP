# Core packages
import streamlit as st
#EDA packages
import pandas as pd
import numpy as np

#Utils
import joblib

def main():
    menu = ["Home","Monitor","About"]

    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Home-Emotion In Text")

    elif choice == "Monitor":
        st.subheader("Monitor App")
         
    else:
        st.sunheader("About") 




if __name__ == 'main__':
    main()
