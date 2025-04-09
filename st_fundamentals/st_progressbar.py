import streamlit as st
import time

st.write("# Progress Bar Example")
st.write("Starting and extenseive computation...")
latest_iteration = st.empty()
progress_text = "Operation in progress...Please Wait.."
my_bar = st.progress(0, text=progress_text)
time.sleep(2)
for i in range(100):
    my_bar.progress(i + 1, text=progress_text)
    time.sleep(0.05)
    latest_iteration.text(f"Iteration {i+1}")

st.write("...and now we're done!")
