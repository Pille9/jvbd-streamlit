import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image

def main():
    st.markdown(
    """
    <style>
    body {
        background-image: url("");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    st.title('Honey bee or Bumble bee?')
    st.write('We help you identifying the genus of the bee you have seen...\n')
    st.write('Press Start and upload your image')
    imagen = Image.open('/workspaces/jvbd-streamlit/hb_bb.JPG')
    st.image(imagen, use_container_width=True)
    
    if st.button('Start', icon='🐝'):
        switch_page('prediction')

if __name__ == "__main__":
    main()