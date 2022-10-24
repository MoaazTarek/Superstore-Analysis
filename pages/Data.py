# importing neede libraries
import MEDA as md
import streamlit as st

# Title
st.markdown(" <center>  <h1> Superstore Dataset </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)

# Link of Data
st.markdown('<a href="https://www.kaggle.com/datasets/vivek468/superstore-dataset-final"> <center> Link to Dataset  </center> </a> ', unsafe_allow_html=True)

# Load data
df = md.df_source

# Show data
st.write(df)
st.write(df.shape)
