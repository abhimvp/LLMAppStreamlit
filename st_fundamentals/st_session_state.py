import streamlit as st

st.title("Streamlit Session")
st.write(st.session_state)
st.write(
    "Think of session_state as a dictionary, you can add a key value pair to the state to remember the history of different widgets values and parameters when your app reruns."
)

if "counter" not in st.session_state:
    st.session_state["counter"] = 0
else:
    st.session_state.counter += 1

st.write(f"Counter: {st.session_state.counter}")

button = st.button("update state")
if "clicks" not in st.session_state:
    st.session_state["clicks"] = 0

if button:
    st.session_state.clicks += 1
    f"After pressing button {st.session_state}"

# connect widget value to session_state
name = st.text_input("What's your name?", key="name")

my_slider = st.slider("Temperature", 0, 100, 50, 1, key="slider")
