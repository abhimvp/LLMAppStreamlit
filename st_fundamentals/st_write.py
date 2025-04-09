import streamlit as st
import pandas as pd

# Displaying data on the screen
# st.write() & Magic

st.title("Displaying data using st.write() and Magic")
st.header("Displaying data using st.write() and Magic")
st.write("we learn streamlit")

l1 = [1, 2, 3, 4, 5]
st.write(l1)

l2= list('abc')
d1 = dict(zip(l1, l2) )
st.write(d1)

# using magic

'Displaying using Magic and displaying smiley using streamlit emoji :100: shortcodes :smile: & :copyright: '

# display pandas dataframe using magic

df = pd.DataFrame({
    'Name': ['Ankit', 'Amit', 'Anuj'],
    'Marks': [60, 80, 70],
    'Package': [12, 16, 14]
})

df # magic - equivalent to st.write