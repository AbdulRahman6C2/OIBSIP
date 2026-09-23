# Retail Sales Exploratory Data Analysis

Exploratory data analysis of a retail/e-commerce sales dataset completed for the Oasis Infobyte Data Analytics internship, Level 1 Task 1.

## Project Overview

The notebook combines order, customer, and product data to investigate:

- Sales trends by month, quarter, and season
- Customer demographics and geographic distribution
- Product categories, pricing, and inventory levels
- Delivery time and order-status patterns
- Payment-method performance
- Relationships between order value, delivery time, ratings, and other numeric measures

The analysis ends with business recommendations around seasonal planning, electronics merchandising, and delivery speed.

## Repository Contents

| File | Description |
| --- | --- |
| `Retail_Sales_EDA .ipynb` | Main Jupyter notebook containing the EDA, visualizations, observations, and recommendations |
| `order.csv` | Order-level data, including dates, status, shipping details, payment method, and total amount |
| `customer.csv` | Customer master data, including names, contact details, country, date of birth, and gender |
| `product.csv` | Product catalog data, including category, supplier, price, stock, reorder level, and discontinued status |
| `clander.csv` | Calendar-style data with date parts, quarter, weekday, week number, and season fields |
| `exec_notebook.py` | Helper script intended to execute the notebook programmatically |

> The current notebook reads `order.csv`, `customer.csv`, and `product.csv` directly. The calendar file is included as a supplementary dataset but is not currently loaded by the notebook.

## Requirements

- Python 3.9 or newer
- Jupyter Notebook or JupyterLab
- pandas
- matplotlib
- seaborn

To install the notebook dependencies:

```bash
python -m pip install pandas matplotlib seaborn jupyter
```

To use `exec_notebook.py`, also install:

```bash
python -m pip install nbformat nbclient
```

## Getting Started

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Install the dependencies listed above.
4. Start Jupyter:

```bash
jupyter notebook
```

5. Open `Retail_Sales_EDA .ipynb` and run the cells from top to bottom.

Keep the CSV files in the same directory as the notebook because the data is loaded using relative paths.

## Running the Notebook from Python

The helper script can execute a notebook without opening Jupyter:

```bash
python exec_notebook.py
```

Before using it from this project directory, update the `path` variable in `exec_notebook.py` to point to the local notebook file. The current value references a notebook in a different directory, and the notebook filename includes a space before `.ipynb`, so quote or use a raw string path when needed.

## Typical Data Workflow

1. Load the order, customer, and product CSV files with pandas.
2. Parse order and shipping dates.
3. Join orders to customer attributes using `CustomerID`.
4. Derive time-based and delivery metrics.
5. Aggregate values by time period, customer segment, category, order status, and payment method.
6. Visualize the results with matplotlib and seaborn.
7. Interpret the findings and turn them into business recommendations.

## Notes

- The CSV files contain personally identifying customer fields such as names, email addresses, phone numbers, and addresses. Handle and share them according to the applicable privacy requirements.
- Run the notebook in its original order because later cells depend on data frames created earlier.
- Generated charts are displayed inline in the notebook; no separate output directory is currently configured.

## Author

Created as part of the Oasis Infobyte Data Analytics internship, Level 1 Task 1.
