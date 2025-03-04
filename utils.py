import pickle
import streamlit as st
import base64
##from tensorflow.keras.models import load_model
##import tensorflow as tf

def predict_genus(imagen):
    # Cargar el modelo
    # realizar predicción
    return '🚧⚠️**Estamos en mantenimiento**⚠️🚧'

def set_background(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

