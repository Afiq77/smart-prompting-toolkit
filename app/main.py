# app/main.py

import streamlit as st
from utils.prompt_runner import run_prompt
import os

st.set_page_config(page_title="Smart Prompting Toolkit")
st.title("🧠 Smart Prompting Toolkit")

prompt_dir = "prompts"
prompt_files = [f for f in os.listdir(prompt_dir) if f.endswith(".txt")]

if not prompt_files:
    st.warning("No prompt templates found in the 'prompts/' folder.")
else:
    selected_prompt = st.selectbox("Choose a prompt template", prompt_files)
    user_input = st.text_area("Enter input text or variable")

    if st.button("Run Prompt"):
        with open(os.path.join(prompt_dir, selected_prompt), "r", encoding="utf-8") as f:
            prompt_template = f.read()

        output = run_prompt(prompt_template, user_input)
        st.subheader("LLM Output")
        st.write(output)
