import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

# Load the model
@st.cache(allow_output_mutation=True)
def load_model():
    model = tf.keras.models.load_model("artifacts/training/model.h5")
    return model

model = load_model()

# Streamlit app title
st.write("""
    # Image Classification
    """)

# File uploader for image input
file = st.file_uploader("Please upload a flower image", type=["jpg", "png", "jpeg"])

# Slider for image size
image_size = st.sidebar.slider("Select Image Size", 100, 500, 224, step=10)

# Function to preprocess and predict
def import_and_predict(image_data, model):
    size = (image_size, image_size)
    image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
    img = np.asarray(image)
    img_reshape = img[np.newaxis, ...]
    prediction = model.predict(img_reshape)
    return prediction

# Display prediction and statistics
if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)

    predictions = import_and_predict(image, model)
    class_names = ["Cat", "Dog"]
    class_index = np.argmax(predictions)
    max_probability = np.max(predictions)
    
    # Display class prediction
    st.success(f"This Image most likely is: {class_names[class_index]}")
    
    # Display prediction probabilities
    st.write("Prediction Probabilities:")
    for i, class_name in enumerate(class_names):
        st.write(f"{class_name}: {predictions[0][i]:.2%}")
    
    # Display overall statistics
    st.write("Prediction Statistics:")
    st.write(f"Max Probability: {max_probability:.2%}")
    st.write(f"Total Sum of Probabilities: {np.sum(predictions):.2%}")

    # Additional statistics or visualizations can be added here
