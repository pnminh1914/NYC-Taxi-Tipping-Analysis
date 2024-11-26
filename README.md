[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Yi0Zbe2y)
# MAST30034 Project 1 README.md
- Name: Ngoc Minh Pham 
- Student ID: 1312628

**Research Goal:** My research goal is finding the best area for yellow taxi drivers with respect to tip over distance.

**Timeline:** The timeline for the research area is for entire year 2023.

Before following below pipeline, make sure you have:
1. Download the taxi zone shapefile from `https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page` and place in `data/taxi_zones`.
2. Download the NYC Central Park weather data from `https://shorturl.at/h23FW` and place in `data/weather` as `weather_central_park.csv`.

To run the pipeline, please run the files in order:
1. `download.py` in `scripts`: This script downloads the raw data into the `data/landing` directory. 
2. `preprocessing_1.ipynb` in `notebooks`: This notebook filters invalid entries and outputs to the `data/raw` directory.
3. `preprocessing_weather.ipynb` in `notebooks`: This notebook reads the original weather data, processes, and outputs to the `data/weather` directory.
4. `preprocessing_2.ipynb` in `notebooks`: This notebook removes excess columns, maps to zones, merges the weather_data and outputs them to the `data/curated` directory.
5. `visualisation.ipynb` in `notebooks`: This notebook visualises data distributions and correlation matrices.
6. `modelling.ipynb`in `notebooks`: This notebook transforms data, fits, predicts and evaluates models.

In notebooks, the first block's purpose is to change the `JAVA_HOME` directory for my environment. Please `DO NOT` run this block.