# Space Detector

## Authors

- Nicolas Deronsart
- Clément Bonduelle

## Description

This is the final project in the Big Data module, the objective is to, to a given picture, tell if there is a galaxy.\
The pictures for the model training will be retrieved from [Hubble Website](https://esahubble.org/images/), we will only use Hubble pictures to ensure picture quality.

In this website, pictures are labelled in the `Object description` field. The training dataset will be constructed by labelling whether if the `Object description` contains the word `galaxy` or not.

The model will be served on an online website that will allow to upload a picture and get a response telling if a galaxy is in it or not.

## Objective

The objective of this project is to automatically label [James Webb Space Telescope](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope) pictures in order to see if a new picture contains relevant information or if you can discard it.

## Project structure

The project is structured as follows:

```
.
├── data
│   ├── labelled_pictures.csv
│   └── ...
├── models
│   └── ...
├── notebooks
│   ├── model_design.ipynb
│   └── web_scraping.ipynb
├── src
│   └── web_scraping.py
├── tests
│   └── test_model.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

- `data`: contains the data used for training.
    - `labelled_pictures.csv`: contains the labelled pictures.
    - `jpg files`: the pictures in jpg format.
- `models`: contains the trained models.
- `notebooks`: contains the notebooks used for the project.
    - `model_design.ipynb`: the notebook used to design the model.
    - `web_scraping.ipynb`: the notebook used to design the data scraping.
- `src`: contains the code source of the project.
    - `web_scraping.py`: the module used to scrap the data.
- `tests`: contains the tests for the project.
    - `test_model.py`: the tests for the model.
- `.env`: the environment variables.
- `.gitignore`: the gitignore file.
- `README.md`: the readme file.
- `requirements.txt`: the requirements file.

## Installation

To use this project, you can create a venv using : `python3 -m venv env`, then you can activate it using `env\Scripts\activate.bat` on Windows or `env/bin/activate` on Unix and then install the dependencies using `pip install -r requirements.txt`.

## Get the data

To get the images, you can run the `web_scraping.py` script using `python src/web_scraping.py` from the root folder. It will download the NB_IMAGES_TO_DOWNLOAD first images from the Hubble website and save them in the `data` folder, while creating a csv file with the images associated to their labels. NB_IMAGES_TO_DOWNLOAD is an environment variable that can be set to change the number of images to download defined in the .env file.
