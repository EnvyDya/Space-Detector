import streamlit as st
import requests

import matplotlib.pyplot as plt
import cv2

import os


API_URL = os.environ.get('API_URL')


st.title('Galaxy.net')

tabs = ['Images', 'Upload new image']

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", tabs)

if selection == 'Upload new image':
    img_area = st.file_uploader(label='Upload your image here',
                                type=['png', 'jpg', 'jpeg'])

    if img_area is not None:
        img = plt.imread(img_area)
        img_resized = cv2.resize(img, (300, 300))
        st.image(img, caption='Uploaded Image', use_column_width=True)
        if st.button('Predict'):
            response = requests.post(f'{API_URL}/predict',
                                     json={"images": [img_resized.tolist()]})
            if response.status_code == 200:
                st.success(f'Galaxy ? {response.json()["galaxies"][0]}')
            else:
                st.error('Error: Something went wrong')
