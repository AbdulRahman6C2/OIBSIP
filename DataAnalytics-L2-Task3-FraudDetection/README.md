# Fraud Detection Project

This project focuses on detecting fraudulent credit card transactions using a highly imbalanced dataset. It is part of the Oasis Infobyte Data Analytics internship task for Level 2, Task 3.

## Overview

The notebook analyzes the well-known Kaggle credit card fraud dataset and builds a machine learning pipeline to identify fraudulent transactions while handling severe class imbalance.

Key objectives include:
- exploring the dataset and identifying class imbalance
- performing exploratory data analysis (EDA)
- preparing features for training
- applying resampling techniques such as SMOTE
- evaluating model performance using fraud-focused metrics

## Dataset

The project uses the file `creditcard.csv`, which contains anonymized transaction data with the following fields:
- `Time`: seconds elapsed since the first transaction
- `Amount`: transaction amount
- `V1` to `V28`: anonymized PCA-transformed features
- `Class`: target label (`0` = legitimate, `1` = fraud)

> The dataset is large and is expected to be placed in the project root directory before running the notebook.

## Project Structure

- `Fraud_Detection.ipynb` — main analysis and modeling notebook
- `creditcard.csv` — dataset used for training and evaluation
- `README.md` — project overview and instructions
- `.gitignore` — ignores local environment, notebooks, and generated files

## Tech Stack

- Python
- pandas
- NumPy
- Matplotlib
- Seaborn
- scikit-learn
- imbalanced-learn

## Setup

1. Create and activate a Python virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn jupyter
   ```

3. Place the dataset file `creditcard.csv` in the project root.

4. Open the notebook:
   ```bash
   jupyter notebook Fraud_Detection.ipynb
   ```

## Notebook Workflow

The notebook covers:
- data loading and inspection
- class imbalance analysis
- descriptive statistics and visual exploration
- train/test split
- feature scaling
- oversampling with SMOTE
- model training and comparison
- evaluation using precision, recall, F1-score, confusion matrix, and ROC-AUC

## Notes

Because fraud cases are extremely rare in this dataset, accuracy alone is not a reliable metric. The project emphasizes metrics that better reflect fraud detection performance, especially recall and precision for the fraud class.

## License

This project is intended for educational and internship use. Please check the dataset source and any applicable licensing terms before reuse or publication.
