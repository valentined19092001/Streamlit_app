# Streamlit_app

# 🌸 Iris Dataset Explorer

## Description
The **Iris Dataset Explorer** application is an interactive graphical interface built with Streamlit that allows users to explore the famous **Iris dataset**. This application enables the visualization of the characteristics of different iris species using interactive plots.

To run the application, you need to install Streamlit. You can do this by running the command `pip install streamlit` in your terminal. Once Streamlit is installed, launch the application with the command `streamlit run iris_app.py`.

## Features
- Filter data by iris species.
- Visualize the relationship between sepal length and petal length.
- Display the distribution of sepal and petal widths.
- Explore filtered data in an expandable section.

## Prerequisites
- Python 3.x
- Streamlit

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/valentined19092001/Streamlit_app.git
   cd Streamlit_app

## Docker Usage

This project is containerized using Docker. To run the application in a Docker container, follow these steps:

1. Build the Docker image:
   ```bash
   docker build -t iris_explorer .
   docker run -p 8501:8501 iris_explorer
  # and then an URL pop up and you just have to copy paste the good one ! :) 
  # this one on my computer : http://localhost:8501
