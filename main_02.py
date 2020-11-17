import streamlit as st
import requests
from PIL import Image
import json
from PIL import ImageDraw

# set to your own subscription key value
subscription_key = '144b7aa4efa94ec1ae859eab12580946'
assert subscription_key
# replace <My Endpoint String> with the string from your endpoint URL
face_api_url = 'https://20201011imanishi.cognitiveservices.azure.com/face/v1.0/detect'

# st.title('My first app')
st.write("""
# 顔認識アプリ
""")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    _img = img
    with io.BytesIO() as output:
        _img.save(output, format="JPEG")
        binary_img = output.getvalue()  # バイナリ取得
    # headers = {'Ocp-Apim-Subscription-Key': subscription_key}
    headers = {'Content-Type': 'application/octet-stream',
              'Ocp-Apim-Subscription-Key': subscription_key}
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    }
    res = requests.post(face_api_url, params=params,
                        headers=headers, data=binary_img)
    result = res.json()
    rect = result[0]['faceRectangle']

    draw = ImageDraw.Draw(img)
    draw.rectangle([(rect['left'], rect['top']), (rect['left']+rect['width'], rect['top']+rect['height'])], fill=None, outline='green',  width=5)

    st.image(img, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    # st.write("Classifying...")
    # label = predict(uploaded_file)
    # st.write('%s (%.2f%%)' % (label[1], label[2]*100))
