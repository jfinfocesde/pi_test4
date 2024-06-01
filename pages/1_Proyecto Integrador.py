import streamlit as st
import pandas as pd


df = pd.read_excel('static/datasets/app3.xlsx')

st.table(df.head(10))