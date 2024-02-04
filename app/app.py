import streamlit as st
import pandas as pd

st.header("Streamlit Deployment Test", False, divider="rainbow")

cities_df = pd.read_csv("../assets/cities.csv", dtype=str)
oscarsm_df = pd.read_csv("../assets/oscar_age_male.csv", dtype=str)
oscarsf_df = pd.read_csv("../assets/oscar_age_female.csv", dtype=str)

st.subheader("Example Cities")
st.write(cities_df)
st.subheader("Oscar Winners - Male")
st.write(oscarsm_df)
st.subheader("Oscar Winners - Female")
st.write(oscarsf_df)