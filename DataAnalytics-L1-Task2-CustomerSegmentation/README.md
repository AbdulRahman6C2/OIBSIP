# E-commerce Sales Analytics and Customer Segmentation

Exploratory retail sales analysis and RFM-based customer segmentation completed for the Oasis Infobyte Data Analytics internship.

## Project Overview

This project analyzes a linked e-commerce dataset covering orders from 2021 to 2025. It is organized into two complementary notebooks:

- **Retail sales EDA:** explores sales trends, customer demographics, product performance, profitability, delivery experience, and returns.
- **Customer segmentation:** uses Recency, Frequency, and Monetary (RFM) features with K-Means clustering to identify groups of customers with different engagement and value profiles.

## Repository Contents

| File | Description |
| --- | --- |
| `Retail_Sales_EDA.ipynb` | Exploratory analysis and business recommendations for retail sales. |
| `Customer_Segmentation_RFM.ipynb` | RFM feature engineering, K-Means clustering, cluster profiling, and marketing recommendations. |
| `ecommerce_sales_customer_analytics_150k.csv` | Consolidated order-level dataset with customer, logistics, marketing, and financial fields. |
| `order_items.csv` | Order line items linked by `order_id` and `product_id`. |
| `product_catalog.csv` | Product, category, brand, supplier, and pricing information. |
| `customer_master.csv` | Customer dimension table with demographics and acquisition cost. |

## Dataset at a Glance

- 138,116 orders from 2021-2025
- 24,911 customers represented in the order data
- 397,569 order line items
- 1,175 catalog products
- 25,000 customer master records
- Fully populated join keys for the relational analysis

The consolidated order dataset includes order status and dates, customer demographics, sales channel, payment and delivery information, returns, ratings, marketing fields, sales, costs, profit, and customer lifetime value.

## Analysis Workflow

### 1. Retail Sales EDA

`Retail_Sales_EDA.ipynb` performs:

1. Dataset loading and missing-value inspection
2. Descriptive statistics for customer age, quantity, sales, profit, margins, delivery, and CLV
3. Monthly and quarterly sales trends
4. Customer age, gender, and declared-segment analysis
5. Product and category revenue analysis using relational joins
6. Correlation analysis for numerical business metrics
7. Delivery performance versus customer rating
8. Return-rate comparison by sales channel

### 2. RFM Customer Segmentation

`Customer_Segmentation_RFM.ipynb` performs:

1. Removal of cancelled orders from the RFM input
2. Customer-level calculation of:
   - **Recency:** days since the most recent order
   - **Frequency:** number of orders
   - **Monetary:** total net sales
3. Standardization with `StandardScaler`
4. Elbow-method evaluation of K-Means cluster counts
5. Four-cluster K-Means modeling with `random_state=42`
6. Cluster visualization and segment profiling

## Key Findings

### Retail sales

- Q4 is the strongest sales period, with November and December leading and February the weakest month.
- Yearly revenue is broadly stable across 2021-2025, suggesting a mature demand pattern rather than sustained growth.
- Electronics is the leading product category and all ten top products by revenue are Electronics products.
- Customer age is broadly distributed and gender representation is close to balanced, including a meaningful Non-Binary segment.
- Faster delivery is consistently associated with higher customer ratings.
- Return rates are similar across sales channels, so channel alone does not explain return behavior.

### Customer segments

The RFM analysis selects `k=4` and identifies these practical segments:

| Segment | Approx. customers | Profile | Recommended action |
| --- | ---: | --- | --- |
| Champions | 3,968 (16%) | Most recent, frequent, and valuable customers | Retain with VIP benefits and exclusive access. |
| Loyal / Core Customers | 9,179 (37%) | Largest group and dependable revenue base | Use cross-sell and upsell campaigns. |
| Low-Engagement | 7,849 (32%) | Relatively active but lower frequency and spend | Increase basket size and purchase frequency. |
| Deeply Lapsed | 3,880 (16%) | No recent purchase for roughly 2.5 years | Target with win-back campaigns. |

Cluster labels are business interpretations of the model output; cluster numbers themselves are arbitrary.

## Technologies

- Python
- pandas and NumPy
- scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

## Getting Started

1. Clone or download this repository and open the project folder in VS Code or Jupyter.
2. Create or select a Python environment.
3. Install the analysis dependencies:

   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn jupyter
   ```

4. Open and run `Retail_Sales_EDA.ipynb` for the exploratory analysis.
5. Open and run `Customer_Segmentation_RFM.ipynb` for the RFM segmentation.

Both notebooks expect the CSV files to be in the same directory as the notebooks. Run the cells from top to bottom so imports, cleaned data, and derived features are available before the visualization and interpretation cells.

## Methodological Notes

- Cancelled orders are excluded from RFM calculations because they do not represent completed purchases.
- Returned orders remain in the RFM input because the purchase occurred before the later return event.
- RFM features are standardized before K-Means so Monetary values do not dominate distances solely because of their larger numeric scale.
- The analysis is descriptive and clustering-based; the resulting segments should be validated against campaign response and future customer behavior before being used for automated targeting.

## License and Data

This repository is an educational analytics project. The included CSV files are used for analysis within the project and should be handled according to their source and distribution terms.