import pickle
import streamlit as st
import base64
import numpy as np
from tensorflow.keras.models import load_model
import tensorflow as tf
from tensorflow.keras.applications.efficientnet import preprocess_input

@st.cache_resource             #Guardar en cache
def load_trained_model():      #Cargar modelo
    model = load_model("models/modelo_abejas_transfer.keras") 
    return model

def predict_genus(imagen):     
    # Cargar el modelo
    model = load_trained_model()
    # Preprocesar imagen
    imagen_pro = preprocess_image(imagen)
    #Hacer la predicción
    predictions = model.predict(imagen_pro)
    # Extraer el valor escalar
    probabilidad = float(predictions[0])
    genus = "bombus" if probabilidad > 0.5 else "apis"
    return genus

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

def preprocess_image(image):
    if image.mode != 'RGB':
        image = image.convert('RGB')
    img = image.resize((224, 224))  # Redimensionar a 224x224
    img_array = np.array(img)  # Convertir en array
    img_array = np.expand_dims(img_array, axis=0)  # Agregar dimensión batch
    img_array = preprocess_input(img_array)  # Preprocesamiento específico para EfficientNet
    return img_array