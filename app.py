import streamlit as st
from main import run_system

st.title("IntelliAgent - Multi Agent AI System")

user_input = st.text_input("Enter your task:")

if st.button("Run Agents"):
    result = run_system(user_input)
    st.success(result)
