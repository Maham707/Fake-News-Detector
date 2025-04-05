# 📰 Fake News Detector

A simple machine learning based web app that classifies news articles as **real** or **fake** based on their content. Built with Python, Flask, and scikit-learn.

## Features

- Clean, user-friendly interface
- Text preprocessing and TF-IDF vectorization
- Trained Logistic Regression model
- Real-time prediction of fake/real news articles

## How It Works

1. **Data**: Uses the `True.csv` and `Fake.csv` datasets taken from Kaggle
https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

2. **Processing**: Text is cleaned, stopwords, special characters, and white spaces removed, and converted to TF-IDF vectors.

3. **Model**: A Logistic Regression model is trained to detect fake news.

4. **Web Interface**: Enter any news article in the textbox to get an instant prediction.

##  Installation & Run

1. Clone the repo:
   ```bash
   git clone https://github.com/Maham707/Fake-News-Detector.git
   cd Fake-News-Detector
