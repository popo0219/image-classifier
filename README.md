# Cat vs Dog Image Classification using CNN Algorithm

## 1.Overview
This design doc outlines the development of a web application for Image Classification using a synthetic dataset. The application will utilize Deep learning models that:
- Evaluates whether the Image will Cat or Dog based on process parameters, different sizes, orientations, or backgrounds.

- This documentation presents the development of an image classification model using Convolutional Neural Networks (CNN) to distinguish between images of cats and dogs. The model is designed to analyze the unique features of cat and dog images and accurately predict the class of a given input image.

## 2. Motivation
The motivation behind this project is to showcase the power of deep learning algorithms, specifically CNNs, in solving real-world problems such as image classification. By building a robust model that can differentiate between cats and dogs, we aim to highlight the potential applications of such technology in various domains, including automated content filtering and image sorting.

## 3. Success Metrics
The success of the Cat vs Dog Image Classification model will be measured using the following metrics:

- **Accuracy:** The percentage of correctly classified images in the test dataset.
- **Precision:** The ratio of true positive predictions to the total predicted positives.
- **Recall:** The ratio of true positive predictions to the actual positives in the dataset.
- **F1 Score:** The harmonic mean of precision and recall, providing a balance between the two.

## 4. Requirements & Constraints
### 4.1. Functional Requirements
- The model should be able to accurately classify images of cats and dogs.
- Users should be able to upload images for prediction through a user-friendly interface.

### 4.2. Non-functional Requirements
- The model's prediction process should be efficient and responsive.
- The user interface should be intuitive and easy to navigate.
- User-uploaded images should be handled securely and privately.

### 4.3. Constraints
- The model will be implemented using TensorFlow and Keras libraries.
- Deployment will be done using Docker containers and cloud hosting platforms like AWS or Google Cloud.
- Cost considerations should be taken into account for deployment.

### 4.4. Out-of-scope
- Integration with external databases or APIs.
- In-depth analysis of model interpretability.

## 5. Methodology
### 5.1. Problem Statement
The challenge is to create a machine learning model that can accurately classify images of cats and dogs, even in scenarios where the images are of different sizes, orientations, or backgrounds.

### 5.2. Data
The dataset consists of thousands of labeled images of cats and dogs. These images will serve as the basis for training, validation, and testing the CNN model. The images are preprocessed to normalize pixel values and resized to a consistent input size.
- Dataset:- [Cat vs Dog dataset](https://www.kaggle.com/competitions/dogs-vs-cats/data)

### 5.3. Techniques
- **Data Preprocessing:** Normalize pixel values, resize images, and apply data augmentation techniques to enhance model generalization.
- **Convolutional Neural Networks (CNNs):** Utilize a deep learning architecture specialized for image analysis. The CNN layers will capture hierarchical features present in the images.
- **Model Training and Validation:** Train the model on the training dataset and validate its performance on a separate validation set to prevent overfitting.
- **Hyperparameter Tuning:** Experiment with different hyperparameters such as learning rate, batch size, and network architecture to optimize model performance.
- **Model Evaluation:** Evaluate the trained model on a separate test dataset to assess its accuracy and performance metrics.

## 6. Architecture
The architecture of the Cat vs Dog Image Classification model consists of the following components:

- **Input Layer:** Receives input images for classification.
- **Convolutional Layers:** Extract features from the images through convolutional operations.
- **Pooling Layers:** Reduce the spatial dimensions of the feature maps.
- **Flatten Layer:** Convert the 2D feature maps into a 1D vector.
- **Fully Connected Layers:** Perform classification using densely connected layers.
- **Output Layer:** Provides the final prediction probabilities for cat and dog classes.

## 7. Pipeline
![pipe (2)](https://github.com/saibattula93/Image-Classification/assets/116423301/8a3345f0-571a-4cbc-8088-597876f5301e)

The MLOps (Machine Learning Operations) pipeline project is designed to create an end-to-end workflow for developing and deploying a web application that performs data preprocessing, model training, model evaluation, and prediction. The pipeline leverages Docker containers for encapsulating code, artifacts, and both the frontend and backend components of the application. The application is deployed on a amazon web service(AWS) to provide EC2 will be used.

The pipeline follows the following sequence of steps:

1. **Data Collection:** Collect labeled images of cats and dogs from a suitable dataset.
2. **Data Preprocessing:** Preprocess the images by resizing, normalizing pixel values, and applying data augmentation.
3. **Model Development:** Build a CNN model architecture with appropriate layers and units.
4. **Model Training:** Train the CNN model using the preprocessed images and tune hyperparameters.
5. **Model Validation:** Validate the model's performance on a separate validation dataset.
6. **Model Evaluation:** Evaluate the model's accuracy and metrics on a test dataset.
7. **Docker Container:** Deploy the trained model within a Docker container for web access.
8. **User Interface:** Develop a user-friendly interface for users to upload images for classification.
9. **Prediction:** The user-uploaded images are passed through the deployed model for classification.
10. **CI/CD Pipeline:** The trained model and application will be deployed on AWS using Docker for containerization:

- Docker Containers: The model, frontend, and backend components will be encapsulated within Docker containers for consistency and portability.
- Amazon ECS (Elastic Compute Cloud): Containers will be deployed on EC2, a scalable container orchestration - service that manages containerized applications.
- AWS Fargate: Fargate will be used as the compute engine for EC2, abstracting the underlying infrastructure management.

## 8. Conclusion
The Cat vs Dog Image Classification model demonstrates the successful implementation of a Convolutional Neural Network for image classification tasks. By accurately distinguishing between images of cats and dogs, this project showcases the potential of deep learning algorithms in solving real-world problems involving image analysis. Through this project, we aim to inspire further exploration of CNNs and their applications in various domains, while emphasizing the deployment and monitoring aspects using AWS and Docker for reliable and scalable solutions.


## Demo Video 
https://github.com/saibattula93/Image-Classification/assets/116423301/154fa4a6-918e-45d8-9efd-72894bd62ecd
