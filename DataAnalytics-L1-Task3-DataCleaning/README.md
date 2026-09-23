# Perfume Dataset Data Cleaning

A data-cleaning project completed for the **Oasis Infobyte Data Analytics Internship, Level 1 Task 3**. The project transforms a deliberately messy perfume classification dataset into a clean, analysis-ready CSV while documenting the reasoning behind each cleaning decision.

## Objective

Clean and validate a perfume dataset containing product characteristics, commercial attributes, and classification labels. The workflow demonstrates practical handling of:

- Missing values
- Exact duplicate records
- Categorical standardization
- Data type correction
- Statistical outlier detection
- Reproducible export of the cleaned data

## Dataset

The raw dataset contains **70,000 records** and includes:

- Product measurements: longevity, sillage, top-note count, price, and concentration
- Categorical attributes: fragrance family, brand tier, gender target, and perfume category
- Binary attributes: alcohol content and limited-edition status

The dataset has no free-text, ID, or date columns, so text preprocessing, ID conversion, and date parsing are not applicable.

## Project Files

| File | Description |
| --- | --- |
| `Data_Cleaning_Perfume_Dataset.ipynb` | Jupyter Notebook containing the complete cleaning workflow and explanations |
| `perfume_type_classification_dataset.csv` | Original raw dataset |
| `perfume_dataset_cleaned.csv` | Cleaned dataset produced by the notebook |

## Cleaning Workflow

1. **Data quality profiling**: inspect shape, data types, null counts, duplicates, ranges, and descriptive statistics.
2. **Missing-value handling**:
   - `price_usd`: median imputation grouped by `perfume_category`
   - `brand_tier`: missing values replaced with `Unknown`
   - `contains_alcohol`: mode imputation
3. **Duplicate removal**: remove exact duplicate rows and reset the index.
4. **Categorical standardization**: strip whitespace and apply title case to categorical fields.
5. **Outlier detection**: use the 1.5 × IQR rule on numeric columns.
6. **Outlier preservation**: retain plausible outliers and add boolean flag columns instead of deleting or capping values.
7. **Data type correction**: convert binary values to integers and fixed-vocabulary fields to pandas `category` dtype.
8. **Export**: save the final result as `perfume_dataset_cleaned.csv`.

## Results

- Raw rows: **70,000**
- Clean rows: **55,000**
- Exact duplicates removed: **15,000**
- Missing values in addressed fields after cleaning: **0**
- Outlier flag columns added: **5**
- Plausible outliers retained to preserve meaningful premium-product variation

## Requirements

- Python 3.9+
- Jupyter Notebook
- pandas
- numpy

## Running the Notebook

From this project directory, create and activate a virtual environment if needed, then install the dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install pandas numpy jupyter
```

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open `Data_Cleaning_Perfume_Dataset.ipynb` and run the cells from top to bottom. The raw CSV must remain in the same directory as the notebook. The final cell writes or refreshes `perfume_dataset_cleaned.csv`.

## Notes

The notebook intentionally avoids blindly applying generic cleaning rules. For example, price is imputed by perfume category because prices vary substantially between categories, while `brand_tier` uses an explicit `Unknown` value to avoid inventing a business classification. Statistical outliers are flagged for downstream analysis but are not removed when their values remain plausible for real perfume products.
