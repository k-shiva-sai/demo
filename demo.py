import streamlit as st
import PIL
from PIL import Image
import numpy as np
st.title("Image Segmentation")
st.write("okokookko")
path=st.sidebar.file_uploader("Upload an file")
if path!=None:
    image=np.array(Image.open(path))
    st.image(image)