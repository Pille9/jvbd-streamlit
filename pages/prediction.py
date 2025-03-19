import streamlit as st
from PIL import Image
import numpy as np
from utils import predict_genus, preprocess_image, set_background

st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-color: #bcbf17;
    }
    [data-testid="stSidebarNav"]::before {
        content: "🔎 Navigation";
        font-size: 22px;
        font-weight: bold;
        color: black;
        padding: 10px;
        display: block;
    }
    [data-testid="stSidebarNav"] ul {
        display: none;
    }
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)


# Barra lateral personalizada
with st.sidebar:
    #st.image("logo.png", width=150)  # Puedes agregar un logo si lo tienes
    st.page_link("main.py", label="🏠 Home")
    st.page_link("pages/prediction.py", label="🐝 Identify a Bee")

# Título de la aplicación
st.title('Upload your image:')

# Cargar imagen
bee = st.file_uploader('Upload you image', type=["jpg", "jpeg", "png"])

# Al cargar imagen
if bee is not None:
    imagen = Image.open(bee)
    st.image(imagen, caption='Subido correctamente', use_container_width=True)

    # Cuadro de texto para el usuario
    user_guess = st.text_input("What genus do you think it is?")

    # Botón para iniciar
    if st.button('Tell me the genus', icon='🐝'):
        pred = predict_genus(imagen)

        # "a" o "an"
        article = "an" if pred.lower().startswith(("a", "e", "i", "o", "u")) else "a"

        # Mostrar resultados
        if user_guess:
            if user_guess.lower() == pred.lower():
                st.success(f'Correct! 🎉 This bee is {article} {pred}.')
            else:
                st.warning(f'Almost! The correct answer is {pred}.')
        else:
            st.write(f'This bee is {article} {pred}.')
