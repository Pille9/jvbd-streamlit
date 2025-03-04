import streamlit as st
from PIL import Image
import numpy as np
from utils import predict_genus

# Título de la aplicación
st.title('Upload your image:')

# Cargar imagen
bee = st.file_uploader(label='Upload you image', type=["jpg", "jpeg", "png"])

# Al cargar imagen
if bee is not None:
    imagen = Image.open(bee).resize((32,32))
    st.image(imagen, caption='Subido correctamente', use_container_width=True)

    #Convertir imagen a matriz
    imagen = np.array(imagen) / 255.0

    # Botón para iniciar
    if st.button('Tell me the genus', icon='🐝'):
        pred = predict_genus(imagen)

        #Mostrar resultados
        st.write(f'This bee is a: {pred}')