import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
import base64

def main():
    # Imagen de fondo
    with open('background.jpg', "rb") as f:
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
    # ´Título
    st.title('Honey bee or Bumble bee?')
    # Presentación
    st.write('We help you identifying the genus of the bee you have seen...\n')
    st.write('Press Start and upload your image')
    imagen = Image.open('hb_bb.JPG')
    st.image(imagen, use_container_width=True)
    # Pulsar botón
    if st.button('Start', icon='🐝'):
        switch_page('prediction')

if __name__ == "__main__":
    main()