import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import cv2
import numpy as np

# st.set_option('deprecation.showfileUploaderEncoding',False)
# @st.cache(allow_output_mutation=True)
def load_model():
    model = tf.keras.models.load_model("artifacts/training/model.h5")
    return model
model = load_model()

st.write("""
    # Image Classification
         """)

file = st.file_uploader("Please upload an flower image", type=["jpg","png","jpeg"])


def import_and_predict(image_data, model):

    size = (224, 224)
    image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
    img = np.asarray(image)
    img_reshape = img[np.newaxis,...]
    prediction = model.predict(img_reshape)

    return prediction

if file is None:
    st.text("Please upload an image file")

else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    predictions = import_and_predict(image, model)
    class_names = ["Cat","Dog"]
    string = "This Image most likely is: "+class_names[np.argmax(predictions)]
    st.success(string)
