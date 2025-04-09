import streamlit as st


# sidebar
st.sidebar.title("Sidebar - title in sidebar")
st.sidebar.header("Header in sidebar ")
my_select_box = st.sidebar.selectbox("Select country", ["US", "UK", "EU"])
st.sidebar.write("You selected: ", my_select_box)
my_slide = st.sidebar.slider("Select a number", 0, 100, 50)
st.sidebar.write("You selected: ", my_slide)

st.sidebar.divider()
st.sidebar.write("This is a divider")
st.sidebar.write("This is a divider")
st.sidebar.divider()

# columns
col1, col2, col3 = st.columns([0.5, 0.3, 0.2])

import random

data = [random.random() for _ in range(100)]

with col1:
    col1.write("This is column 1")
    st.line_chart(data)

col2.subheader("This is column 2")
col2.write(data[:13])

col3.subheader("This is column 3")


# expander
with st.expander("Click to expand"):
    st.write("This is expanded")
    st.write("This is expanded")
    st.write("This is expanded")

with st.expander("A cool bar_chat"):
    st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})
    st.write("This is expanded")
