import streamlit as st
import pandas as pd

st.title('A Simple Streamlit Web App')

name = st.text_input("Enger your name", '')

st.write(f"Hello {name}!")

# https://discuss.streamlit.io/t/is-there-a-double-sided-slider/11947
# x = st.slider("Select an integer x", 0, 10, 1)
# y = st.slider("Select an integer y", 0, 10, 10)

x,y = st.slider("Select integer range", 0, 10, (1,9))

df = pd.DataFrame({'x':[x], 'y':[y], "x+y": [x+y]}, index=['addition row'])
st.write(df)

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='data.csv',
    mime='text/csv',
)