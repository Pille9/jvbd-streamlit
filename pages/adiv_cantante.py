import streamlit as st
from utils import adivina_cantante

# Título de la aplicación
st.title('Adivina el género musical:')

# Cargar cantante
cantante = st.text_input('Escribe el cantante', max_chars=50)

# Al escribir el cantante
if cantante is not None:

    # Botón para iniciar
    if st.button('Adivinar género musical', icon='🎶'):
        pred = adivina_cantante(cantante)

        #Mostrar resultados
        st.write(f'El género musical es: {pred}')