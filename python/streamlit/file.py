import streamlit as st
import pandas as pd
import time

file = st.file_uploader("파일 업로드", type=['csv', 'xlsx'])

time.sleep(2)

if file is not None:
    ext = file.name.split('.')[1]
    if ext == 'csv':
        data = pd.read_csv(file)
    else:
        data = pd.read_excel(file, engine='openpyxl')

    st.dataframe(data)