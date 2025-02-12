import streamlit as st
from PIL import Image
import numpy as np
from utils import adivina_caratula

# Título de la aplicación
st.title('Adivina el género musical:')

# Cargar imagen
caratula = st.file_uploader('Subir carátula', type=["jpg", "jpeg", "png"])

# Al cargar imagen
if caratula is not None:
    imagen = Image.open(caratula).resize((32,32))
    st.image(imagen, caption='Subido correctamente', use_container_width=True)

    #Convertir imagen a matriz
    imagen = np.array(imagen) / 255.0

    # Botón para iniciar
    if st.button('Adivinar género musical', icon='🎶'):
        pred = adivina_caratula(imagen)

        #Mostrar resultados
        st.write(f'El género musical es: {pred}')