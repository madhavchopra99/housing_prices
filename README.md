# Housing Prices Prediction

A Django web application for predicting house prices in Bengaluru using linear regression.

## Description

This project implements a house price prediction system using linear regression on the Bengaluru House Price dataset from Kaggle. The application provides a web UI built with Django to input house features and get price predictions.

## Features

- Data cleaning and preprocessing
- Linear regression model training
- Django web interface for predictions
- Model persistence with pickle files

## Dataset

The dataset is available on Kaggle: [Bengaluru House Price Data](https://www.kaggle.com/amitabhajoy/bengaluru-house-price-data)

## Project Structure

```
housing_prices/
├── BHM/
│   └── artifacts/
│       └── main.py          # Data processing and model training script
├── screenshot/
│   └── screenshot.png       # Application screenshot
├── housing_prices/          # Django project
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt         # Project dependencies (also managed by uv)
└── pyproject.toml           # Modern dependency management
```

## Installation

1. Clone the repository
2. Create and activate virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies using uv:
   ```bash
   uv sync
   ```

## Running the Application

1. Apply Django migrations:
   ```bash
   uv run python manage.py migrate
   ```

2. Run the development server:
   ```bash
   uv run python manage.py runserver 127.0.0.1:8000
   ```

3. Access the application at `http://127.0.0.1:8000`

## Dependencies

The project uses the following dependencies (managed by uv):
- Django
- pandas
- scikit-learn
- numpy
- matplotlib
- pillow
- and more...

## Usage

Use the web interface to input house features and get price predictions.

## Screenshot

![Application Screenshot](https://raw.githubusercontent.com/madhavchopra99/housing_prices/main/screenshot/screenshot.png)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

