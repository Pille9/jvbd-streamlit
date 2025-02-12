import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image

def main():
    st.markdown(
    """
    <style>
    body {
        background-image: url("https://es.akinator.com/assets/img/akitudes_520x650/defi.png");
        background-size: 400x500;
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    st.title('Adivina el género musical')
    st.write('**Cómo lo quieres adivinar**')
    imagen = Image.open('akinator.webp')
    st.image(imagen, use_container_width=True)
    opcion = st.radio('Selecciona cómo adivinar:', 
                      ('Audio', 'Carátula', 'Cantante'), 
                      index=0, 
                      key='option')
    
    if st.button('Empezar!', icon='🙌'):
        route_prediction(opcion)

def route_prediction(opcion):
    if opcion == 'Audio':
        switch_page("adiv_audio")
    elif opcion == 'Carátula':
        switch_page("adiv_caratula")
    elif opcion == 'Cantante':
        switch_page("adiv_cantante")

if __name__ == "__main__":
    main()