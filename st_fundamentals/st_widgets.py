import streamlit as st
import pandas as pd

# text input

name = st.text_input("Enter your name")
if name:
    st.write(f"Hello {name}")

st.divider()  # horizontal line

# number input

age = st.number_input("Enter your age", min_value=1, max_value=100)
if age:
    st.write(f"Your age is {age}")

st.divider()  # horizontal line

# button

clicked = st.button("Click me")
if clicked:
    st.write(f"Button clicked! :ghost: ")

st.divider()  # horizontal line

# checkbox

agree = st.checkbox("I agree")
if agree:
    st.write("You agreed!")

checked = st.checkbox("I am checked", value=True)
if checked:
    ":+1:" * 5

df = pd.DataFrame(
    {"Name": ["Ankit", "Amit", "Anuj"], "Marks": [60, 80, 70], "Package": [12, 16, 14]}
)
if st.checkbox("Show data"):
    st.write(df)

st.divider()  # horizontal line

# radio button
genders = ["Male", "Female", "Other", "Prefer not to say"]
gender = st.radio("Select your gender", genders, index=3, key="your_selected_gender")
if gender:
    st.write(f"You selected {gender}")
    st.write(
        f"Your selected gender is using (key) session state: {st.session_state.your_selected_gender}"
    )

st.divider()  # horizontal line

# select

country = st.selectbox("Select your country", ["USA", "UK", "India", "Nepal"])
if country:
    st.write(f"You selected {country}")

st.divider()  # horizontal line

# slider

age = st.slider("Select your age", value=1, min_value=12, max_value=78, step=3)
if age:
    st.write(f"You selected {age}")

st.divider()  # horizontal line

# file_uploader

file = st.file_uploader("Upload a file", type=["txt", "csv", "xlsx"])
if file:
    if file.type == "text/plain":
        from io import StringIO

        string_io = StringIO(file.getvalue().decode("utf-8"))
        string_data = string_io.read()
        st.write(string_data)
        # content = file.read().decode('utf-8')
        # st.write(content)
    elif file.type == "application/vnd.ms-excel":
        df = pd.read_excel(file)
        st.write(df)
    elif file.type == "text/csv":
        df = pd.read_csv(file)
        st.write(df)

st.divider()  # horizontal line

# camera_input

camera = st.camera_input("Take a picture")

st.divider()  # horizontal line

# image

st.image("https://picsum.photos/200/300", caption="Sample Image")
