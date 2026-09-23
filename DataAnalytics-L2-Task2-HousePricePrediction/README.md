# House Price Prediction with Linear Regression

An exploratory machine learning project that predicts residential sale prices using linear regression and regularized regression models. The analysis is completed in a Jupyter notebook as part of the Oasis Infobyte Data Analytics internship.

## Project Overview

The project uses a simplified version of the Ames, Iowa housing dataset. It covers:

- Exploratory data analysis and missing-value checks
- Feature selection and correlation analysis
- Feature engineering for house age and years since remodeling
- One-hot encoding of categorical features
- An 80/20 train-test split
- Linear Regression, Ridge, and Lasso model training
- Evaluation with MSE, RMSE, and R²
- Actual-versus-predicted and residual plots
- Raw and standardized coefficient analysis

The source file contains 2,919 properties. Because `SalePrice` is unavailable for the original competition test partition, modeling uses the 1,460 rows with known sale prices.

## Repository Contents

```text
.
├── House_Price_Linear_Regression.ipynb  # Analysis, visualizations, and models
├── HousePricePrediction.csv             # Housing dataset
└── README.md                            # Project documentation
```

## Dataset Features

The dataset includes the following columns:

- `MSSubClass`, `MSZoning`, `LotConfig`, `BldgType`, `Exterior1st`
- `LotArea`, `OverallCond`, `YearBuilt`, `YearRemodAdd`
- `BsmtFinSF2`, `TotalBsmtSF`
- `SalePrice` (target)

`Id` is treated as an identifier and removed before modeling. `MSSubClass` is treated as categorical rather than continuous.

## Requirements

- Python 3.9 or newer
- Jupyter Notebook or JupyterLab
- pandas
- NumPy
- scikit-learn
- matplotlib
- seaborn

## Getting Started

1. Open a terminal in the project directory.
2. Create and activate a virtual environment if needed:

   ```bash
   python -m venv .venv
   ```

   Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

3. Install the dependencies:

   ```bash
   python -m pip install pandas numpy scikit-learn matplotlib seaborn jupyter
   ```

4. Start Jupyter:

   ```bash
   jupyter notebook
   ```

5. Open `House_Price_Linear_Regression.ipynb` and run the cells from top to bottom.

The notebook expects `HousePricePrediction.csv` to remain in the same directory.

## Modeling Workflow

1. Load and inspect the dataset.
2. Keep only rows with a known `SalePrice`.
3. Apply median/mode imputation where necessary.
4. Create `HouseAge` and `YearsSinceRemodel` using 2010 as the reference year.
5. One-hot encode categorical variables with `drop_first=True`.
6. Split the labeled data into training and test sets using `random_state=42`.
7. Train and compare Linear Regression, Ridge, and Lasso models.
8. Inspect errors, residuals, and model coefficients.

## Results and Findings

The plain Linear Regression model achieves approximately:

- Test R²: `0.665`
- Test RMSE: `$50,700`

`TotalBsmtSF` and `HouseAge` are consistently among the strongest predictors. The target is right-skewed, and residual analysis indicates that prediction errors increase for more expensive homes. A future improvement would be to train on `log(SalePrice)` and transform predictions back to dollar values.

The Ridge and Lasso models perform similarly to ordinary Linear Regression. Lasso also demonstrates automatic feature selection by reducing some coefficients to zero.

## Limitations and Future Improvements

This simplified dataset does not include several strong predictors from the full Ames dataset, such as neighborhood, room and bathroom counts, garage details, and overall quality. Further improvements could include:

- Using the complete Ames feature set
- Applying a log transformation to `SalePrice`
- Comparing additional nonlinear models
- Using cross-validation and hyperparameter tuning
- Adding a reusable prediction script or deployment interface
