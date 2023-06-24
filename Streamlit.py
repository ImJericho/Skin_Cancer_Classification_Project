import streamlit as st
import numpy as np
from PIL import Image
import cv2
import tensorflow 

from tensorflow.keras.metrics import top_k_categorical_accuracy
def top_3_accuracy(y_true, y_pred):
    return top_k_categorical_accuracy(y_true, y_pred, k=3)

def top_2_accuracy(y_true, y_pred):
    return top_k_categorical_accuracy(y_true, y_pred, k=2)


MODEL = tensorflow.keras.models.load_model("./model_v3.h5", custom_objects = {"top_2_accuracy":top_2_accuracy, "top_3_accuracy":top_3_accuracy})
CLASS_NAMES = ["Bowen's disease (akiec)","basal cell carcinoma (bcc)","benign keratosis-like lesions/solar lentigines (bkl)","dermatofibroma (df)","melanoma (mel)","melanocytic nevi (nv)","vascular lesions/hemorrhage (vasc)"]


st.title("SKIN CANCER CLASSIFICATION")
# st.markdown("<h1 style='text-align: center; color: gray;'><B>PATATO DISEASE CLASSIFICATION</B></h1>", unsafe_allow_html=True)
st.write("*..............................This Project was owned by* Vivek Patidar *all the licence belongs to him................................*")


option = st.selectbox('Select input method :', ['Camera','Gallary'])

if(option=='Gallary'):
    # taking image as input
    image_type = st.selectbox('select image type',['jpg','png','jfif'])
    uploaded_file = st.file_uploader("Choose an image...", type=image_type)

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=False)
        image = np.array(image)
        image = np.expand_dims(image, 0)
        st.write("Classifying............")
        st.write(".")
        st.write(".")
        
        predictions = MODEL.predict(image)
        prediction = np.argmax(predictions)
        confidence = np.max(predictions)
        
        
        # st.markdown("<h2 style='text-align: center; color: gray;'><B>CANCER TYPE:</B></h2>", unsafe_allow_html=True)
        st.write('Cancer Name : %s' %(CLASS_NAMES[prediction]))
        st.write('Confidence = %f percentage' %(confidence*100))

else:
    # #taking live camera input
    img_file_buffer = st.camera_input("Take The Picture Of The Skin")
    if img_file_buffer is not None:
        # To read image file buffer with OpenCV:
        bytes_data = img_file_buffer.getvalue()
        image = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
        image.resize((224,224,3))

        # st.image(image, caption='Uploaded Image.', use_column_width=True)
        image = np.array(image)
        image = np.expand_dims(image, 0)
        # st.write(type(image))
        # image.reshape(224,244,3)
        
        st.write("Classifying............")
        st.write(".")
        st.write(".")
        predictions = MODEL.predict(image)
        prediction = np.argmax(predictions)
        confidence = np.max(predictions)
        pred = CLASS_NAMES[prediction]
        st.subheader('Cancer Name : %s' %(CLASS_NAMES[prediction]))
        st.subheader('Confidence : %f percentage' %(confidence*100))