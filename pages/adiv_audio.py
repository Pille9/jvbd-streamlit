import streamlit as st
from utils import adivina_audio

# Título de la aplicación
st.title('Adivina el género musical:')

# Cargar audio
audio = st.file_uploader('Subir audio', type=["wav"])



# Al cargar audio
if audio is not None:
    # Cargar audio
    audio_bytes = audio.read()
    st.audio(audio_bytes)

    # Botón para iniciar
    if st.button('Adivinar género musical', icon='🎶'):
        pred = adivina_audio(audio_bytes)

        #Mostrar resultados
        st.write(f'El género musical es: {pred}')