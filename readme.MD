# Space Detector

## Authors

- Nicolas Deronsart
- Clément Bonduelle

## Description

This is the final project in the Big Data module, the objective is to, to a given picture, tell if there is a galaxy.\
The pictures for the model training will be retrieved from [Hubble Website](https://hubblesite.org/images).

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
|   |-- pictures
|   |   |-- ...
|   |-- labelled_pictures.csv
|-- notebooks
|   |-- ...
|-- tests
|   |-- ...
|-- requirements.txt
```

- `bin`: contains the scripts to run the project
- `models`: contains the trained models
- `data`: contains the data used for training
- `notebooks`: contains the notebooks used for the project
- `tests`: contains the tests for the project
- `requirements.txt`: contains the dependencies for the project
