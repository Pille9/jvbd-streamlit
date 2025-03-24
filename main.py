import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
import base64
from utils import set_background

def main():
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {
            background-color: #8dbf17;
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

    # Imagen de fondo
    set_background('image.jpg')
    # ´Título
    st.title('Honey bee or Bumble bee?')
    # Presentación
    st.write('We assist you in determining if your bee belongs to the honey bee or bumble bee genus.\n')
    st.write('Press Start and upload your image')
    imagen = Image.open('hb_bb.png')
    st.image(imagen, use_container_width=True)
    # Pulsar botón
    if st.button('Start', icon='🐝', type='tertiary'):
        switch_page('prediction')
    
    # Barra lateral personalizada
    with st.sidebar:
        #st.image("logo.png", width=150)  # Puedes agregar un logo si lo tienes
        st.page_link("main.py", label="🏠 Home")
        st.page_link("pages/prediction.py", label="🐝 Identify a Bee")

if __name__ == "__main__":
    main()