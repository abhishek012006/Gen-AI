import streamlit as st
import pandas as pd
st.title("Streamlit Text Input")

name=st.text_input("enter ur name: ")

age=st.slider("select your age:",0,100,25)

options=["python","java","c++"]
choice=st.selectbox("choose your fav lang: ",options)
st.write(f"you selected {choice}")

st.write(f"your age is: {age}")

if name:
    st.write(f"hello ,{name}")

uploaded_file=st.file_uploader("choose a csv: ",type="csv")

if uploaded_file is not None:
    df=pd.DataFrame(uploaded_file)
    st.write(df)
