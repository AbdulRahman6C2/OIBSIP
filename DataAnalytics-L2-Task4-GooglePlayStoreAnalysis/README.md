# Google Play Store Analysis

This project analyzes public Google Play Store app data to uncover insights about app categories, ratings, reviews, installs, and pricing trends.

## Project Overview

The analysis is implemented in a Jupyter Notebook and uses two datasets:

- `googleplaystore.csv` — app metadata such as category, rating, reviews, size, installs, type, price, and content rating
- `googleplaystore_user_reviews.csv` — user review sentiment and feedback data

## Goals

- Clean and explore the dataset
- Identify trends in app ratings and popularity
- Examine category-wise performance
- Understand review patterns and user sentiment
- Present findings through visualizations and summary insights

## Files in this Project

- `Google_Play_Store_Analysis.ipynb` — main analysis notebook
- `googleplaystore.csv` — app dataset
- `googleplaystore_user_reviews.csv` — review dataset
- `README.md` — project documentation
- `.gitignore` — Git ignore rules for Python/Jupyter project files

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

Install the required dependencies:

```bash
pip install jupyter pandas numpy matplotlib seaborn
```

## Run the Project

Open the notebook in Jupyter:

```bash
jupyter notebook
```

Then open `Google_Play_Store_Analysis.ipynb` and run the cells in order.

## Notes

This project is intended for data exploration and analysis tasks related to mobile app market trends. It can be extended with additional visualizations, machine learning models, or dashboard-style reporting.
