import streamlit as st
#from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests
from PIL import Image
import io
import joblib
from abcd import predict
import pandas as pd


st.title('Microsoft Recommendation Algorithms')

# Models
rlrmc = open("RLRMC.SAV","rb")
rlrmc_model = joblib.load(rlrmc)
    
#image = Image.open('snack.jfif')

#st.image(image, caption='Snack Recommendation',use_column_width=True)

title = st.number_input('User ID',min_value = 0,max_value=1000,value = 0,step =1)

pro = st.number_input('Snack ID',min_value = 0,max_value=1000,value = 0,step =1)

#Type = st.selectbox(
#        "Choose Snack Type",["Diet", "Keto","Meats","Vegetarian","Vegan"])
url = 'http://127.0.0.1:8000/'
endpoint = 'predict/'

def get_data(user_id,pro_id):
    server_url = url + endpoint + str(user_id) + ',' + str(pro_id)
    r= requests.get(server_url)
    return r.json()


if st.button('Prediction Search'):
    #st.write('hello')
    segments = get_data(title,pro)
    st.write(segments)
    data = pd.read_csv('LightGCN.csv')  
    df1 =  data['userID']==title
    df2 =data[df1]
    if df2.empty:
        st.write('we have no information on this user!')
        #image = Image.open('no.jfif')
        #st.image(image,use_column_width=True)
    else:
        #image = Image.open('foru.png')
        #st.image(image,use_column_width=True)
        st.write(df2['Snack_Name'])
