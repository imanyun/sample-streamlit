import streamlit as st
import pandas as pd
from sklearn import datasets
from PIL import Image

# st.title('My first app')
st.write("""
# 顔認識アプリ
""")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    # st.write("Classifying...")
    # label = predict(uploaded_file)
    # st.write('%s (%.2f%%)' % (label[1], label[2]*100))
