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

```bash
|-- bin
|-- models
|-- data
|   |-- labelled_pictures.csv
|   |-- ...
|-- notebooks
|   |-- web_scraping.ipynb
|-- tests
|   |-- ...
|-- requirements.txt
|-- .gitignore
```

- `bin`: contains the scripts to run the project
    - `web_scraping.py`: contains the module used to scrap the data
- `models`: contains the trained models
- `data`: contains the data used for training (will be filled at the launch of web scraping)
- `notebooks`: contains the notebooks used for the project
    - `web_scraping.ipynb`: contains the notebook used to scrap the data
- `tests`: contains the tests for the project
- `requirements.txt`: contains the dependencies for the project
- `.gitignore`: contains the files to ignore for git

## Installation

To use this project, you can create a venv using : `python3 -m venv env`, then you can activate it using `env\Scripts\activate.bat` on Windows or `en/bin/activate` on Unix and then install the dependencies using `pip install -r requirements.txt`.