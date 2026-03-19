import streamlit as st
import requests

st.title("DevAssist AI - Developer Assistant")

task = st.selectbox(
    "Select Task",
    ["explain", "bugs", "improve", "commit", "score"]
)

code = st.text_area("Paste your code here")

if st.button("Analyze Code"):

    response = requests.post(
        "http://127.0.0.1:8000/analyze",
        json={"code": code, "task": task}
    )

    result = response.json()

    st.subheader("AI Response")
    st.write(result["result"])