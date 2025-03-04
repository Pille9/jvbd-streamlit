import streamlit as st
from PIL import Image
import numpy as np
from utils import predict_genus

# Título de la aplicación
st.title('Upload your image:')

# Cargar imagen
bee = st.file_uploader('Upload you image', type=["jpg", "jpeg", "png"])

# Al cargar imagen
if bee is not None:
    imagen = Image.open(bee).resize((32,32))
    st.image(imagen, caption='Subido correctamente', use_container_width=True)

    #Convertir imagen a matriz
    imagen = np.array(imagen) / 255.0

    # Cuadro de texto para el usuario
    user_guess = st.text_input("What genus do you think this is?")

    # Botón para iniciar
    if st.button('Tell me the genus', icon='🐝'):
        pred = predict_genus(imagen)

        #Mostrar resultados
        if user_guess:
            if user_guess.lower() == pred.lower():
                st.success(f'Correct! 🎉 This bee is a {pred}.')
            else:
                st.warning(f'Almost! The correct answer is {pred}.')
        else:
            st.write(f'This bee is a: {pred}')