# Space Detector

## Authors

- Nicolas Deronsart
- Clément Bonduelle

## Description

This is the final project in the Big Data module, the objective is to, to a given picture, tell if there is a galaxy.
The pictures for the model training will be retrieved from [Hubble Website](https://esahubble.org/images/), we will only use Hubble pictures to ensure picture quality.

In this website, pictures are labelled in the `Object description` field. The training dataset will be constructed by labelling whether if the `Object description` contains the word `galaxy` or not.

The model will be served on an online website that will allow to upload a picture and get a response telling if a galaxy is in it or not.

## Objective

The objective of this project is to create a collaborative website `Galaxy.net` where people can add pictures of galaxies. To ensure that the pictures are relevant, we use a model to predict if they contain a galaxy or not.  

A model can be automatically trained using the [James Webb Space Telescope](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope) pictures.

## Project structure

The project is structured as follows:

```
.
├── data
│   ├── labelled_pictures.csv
│   └── ...
├── models
│   └── galaxy_classifier-v{...}.pt
├── notebooks
│   ├── model_design.ipynb
│   └── web_scraping.ipynb
├── src
│   ├── model_training
│   │   ├── CNN.py
│   │   └── train_model.py
│   └── web_scraping.py
├── tests
│   └── test_model.py
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── scrap_and_train.sh
```

- `data`: contains the data used for training.
    - `labelled_pictures.csv`: contains the labelled pictures.
    - `jpg files`: the pictures in jpg format.
- `models`: contains the trained models, using the format `galaxy_classifier-v{...}.pt` where `{...}` is the version of the model.
- `notebooks`: contains the notebooks used for the project.
    - `model_design.ipynb`: the notebook used to design the model.
    - `web_scraping.ipynb`: the notebook used to design the data scraping.
- `src`: contains the code source of the project.
    - `model_training`: contains the code used to train the model.
        - `CNN.py`: the model architecture.
        - `train_model.py`: the script used to train the model on the labelled data.
    - `web_scraping.py`: the module used to scrap the data.
- `tests`: contains the tests for the project.
    - `test_model.py`: the tests for the model.
- `.env`: the environment variables.
- `.gitignore`: the gitignore file.
- `README.md`: the readme file.
- `requirements.txt`: the requirements file.

## Installation

To use this project, you can create a venv using : 
```
python3 -m venv env
```

Then you can activate it using the following command on Unix : 
```
env/bin/activate
```

Or if you are on Windows :
```
env\Scripts\activate.bat
``` 

And finally install the dependencies using 
```
pip install -r requirements.txt
```

## Get the data

To get the images, you can run the `web_scraping.py` script using the following command from the root folder : 
```
python src/web_scraping.py
``` 
It will download the 49 images from the Hubble website and save them in the `data` folder, while creating a csv file with the images associated to their labels. 

## Train the model

To train the model, you can run the `train_model.py` script using this command from the root folder : 
```
python src/model_training/train_model.py
``` 
It will train the model on the data in the `data` folder and save the model in the `models` folder. The model will be saved using the format `galaxy_classifier-v{...}.pt` where `{...}` is the version of the model.

## Get the data and train the model

To get the data and train the model, you can run the `scrap_and_train.sh` script using :
```
./scrap_and_train.sh
```
It will run the `web_scraping.py` script and then the `train_model.py` script.
If it doesn't work, you should run : 
```
chmod +x scrap_and_train.sh
```
