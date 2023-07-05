# DermDetect - Skin Cancer Classification Project

DermDetect is a skin cancer classification project that utilizes a neural network model trained on a Kaggle dataset and employs MobileNet transfer learning. The project has been deployed using Streamlit, a web application framework for Python.

Skin cancer is a prevalent disease, and early detection plays a crucial role in its successful treatment. DermDetect aims to assist dermatologists and healthcare professionals in accurately classifying skin lesions as benign or malignant. By leveraging deep learning techniques, DermDetect automates the classification process and provides reliable predictions based on input images.

## Table of Contents
Dataset <br />
Model Architecture<br />
Installation<br />
Usage<br />


## Dataset
The skin cancer dataset used in this project is sourced from Kaggle. It consists of a large collection of skin lesion images categorized into seven classes:<br />

Basal Cell Carcinoma<br />
Melanocytic Nevus<br />
Dermatofibroma<br />
Melanoma<br />
Benign Keratosis<br />
Vascular Lesion<br />
Squamous Cell Carcinoma<br />
This diverse dataset provides a comprehensive representation of various skin conditions, enabling the neural network to learn patterns and make accurate predictions.

## Model Architecture
DermDetect employs MobileNet as the base model for transfer learning. MobileNet is a lightweight convolutional neural network (CNN) architecture optimized for mobile and embedded vision applications. By leveraging transfer learning, the pre-trained MobileNet model is fine-tuned on the skin cancer dataset, enabling it to learn relevant features and improve classification accuracy.

## Installation
To run DermDetect locally, follow these steps:<br />
<br />
Clone the repository:<br />
<br />
bash<br />
Copy code<br />
git clone https://github.com/ImJericho/Skin_Cancer_Classification_Project.git<br />
Navigate to the project directory:<br />
<br />
bash<br />
Copy code<br />
cd Skin_Cancer_Classification_Project<br />
Install the required dependencies using pip:
<br />
bash
Copy code<br />
pip install -r requirements.txt<br />
Download the pre-trained weights for the MobileNet model from this link and place the model_weights.h5 file in the project directory.

## Usage
To use DermDetect, execute the following command:
<br />
<br />
bash<br />
Copy code<br />
streamlit run app.py<br />
This command will start the Streamlit server, and you can access the application by visiting the provided URL in your web browser.

Once the application is launched, you can upload an image of a skin lesion and click the "Classify" button to obtain the predicted class for the lesion. DermDetect will provide you with the probability of the lesion belonging to each of the seven classes mentioned earlier, along with the predicted class label.
