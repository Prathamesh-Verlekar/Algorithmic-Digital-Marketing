#!/usr/bin/env python
# coding: utf-8

# In[3]:

import streamlit as st
st.markdown('<style>body{background-color: Aquamarine;}</style>',unsafe_allow_html=True)
st.title("SEARCH FOR SIMILAR PRODUCTS")
html_temp = """<body style="background-color:grey>
</body>
"""

st.markdown(html_temp,unsafe_allow_html=True)
import glob
from PIL import Image, ImageOps
import numpy as np
import pandas as pd


image = Image.open('alibaba.jpg')

st.image(image,use_column_width=True)

def get_data():
    return pd.read_csv('streamlit.csv',header=None)
n=1
df = get_data()
images = df[0].unique()
st.subheader("Choose a product")
pic = st.selectbox('Products: ', images)
st.subheader("Product Selected")
st.image(pic,width=None)
st.subheader("Similar Products")
for index, row in df.iterrows():
    if row[0]==pic:
        while n < 11:
            st.image(row[n], use_column_width=None, caption=row[n])
            n+=1
