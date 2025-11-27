# Australian Beverage Market Data Analytics (Woolworth vs Coles vs ALDI)
## 📌 Project Overview

This project analyzes the price strategy, promotion depth, and category-level competition in the Australian grocery beverage market (Woolworths, Coles, Aldi).
The workflow covers the full data pipeline:

Web scraping (Python)

Data cleaning & processing (Pandas / Excel)

Exploratory data analysis

Tableau interactive dashboards

Insights for retail pricing & category management

(Raw data is not included due to website policy considerations.
A cleaned, de-identified dataset is provided for reproducibility.)

## 📂 Repository Structure
```
beverage_analysis/
│
├── processing_data/         # Cleaned data + Jupyter Notebook pipeline
│    ├── processing.ipynb    # Full cleaning workflow (Jupyter Notebook)
│    ├── union_drinks.csv    # Final cleaned dataset
├── scraping_open_resource/  # Safe scraping templates (no URLs/tokens)
│    ├── wws.py          
│    ├── coles.py            
│    ├── aldi.py            
├── beverage_analytics.twbx  # Final dashboard
├── record_document/         # Project proposal and report
└── README.md
```

## 🗂️Data collection

This project collected data on beverage products from three major supermarkets in the Sydney area of Australia through python automated scripts.

The original data included 4,349 entries and 11 fields. 

The original data was sourced from the official websites of Woolworth, Aldi, and Coles in Australia, and did not involve login, bypassed permissions, or data storage and distribution. The data is collected from public web pages and is only used for technical learning. It is not involved in commercial purposes or mass redistribution. 

Data acquisition scripts can be found in scraping_open_resource: wws.py, coles.py, aldi.py

Among them, sensitive information and specific urls have been concealed.

## ✂️Data Processing
The full end-to-end data cleaning workflow is documented in:
```
processing_data/processing.ipynb
```
This notebook records every transformation step applied to the raw scraped dataset.

Raw scraped data contained 3,526 rows and the following fields:

| Field               | Description                    |
| ------------------- | ------------------------------ |
| `name`              | Product name                   |
| `brand`             | Brand                          |
| `instore_price`     | Current in-store price         |
| `instore_was_price` | Previous in-store price        |
| `instore_cup_price` | Unit price (in-store)          |
| `online_price`      | Current online price           |
| `online_was_price`  | Previous online price          |
| `online_cup_price`  | Unit price (online)            |
| `cup_measure`       | Unit measure (e.g., 1L, 100mL) |
| `package_size`      | Pack size                      |
| `category`          | Category list from source site |

(Some SKU has missing fields, Here is the greatest common divisor of the fields)
Example raw row:
```
name = Remedy Wild Berry Kombucha 250mL x 4 pack
brand = Remedy
instore_price = 9.5
instore_was_price = 9.5
online_price = 9.5
cup_measure = "1L"
package_size = "250mL x 4 pack"
category = ["Soft Drinks"]
```
Go throw all the steps in processing.ipynb, then I got the clean data structure like this:

| Field             | Description             |
| ----------------- | ----------------------- |
| retailer          | Retailer name           |
| name              | Product name            |
| brand             | Brand                   |
| package_size      | Standardized pack size  |
| instore_price     | Current in-store price  |
| instore_was_price | Previous in-store price |
| online_price      | Current online price    |
| online_was_price  | Previous online price   |
| save_percent      | % discount              |
| category_original | Source category         |
| category_std      | Standardized category   |

Example cleaned output:
```
retailer = Woolworth
name = Remedy Wild Berry Kombucha 250mL x 4 pack
brand = Remedy
package_size = 250mL x 4 pack
instore_price = 9.5
instore_was_price = 9.5
online_price = 9.5
online_was_price = 9.5
save_percent = 0
category_original = ["Soft Drinks"]
category_std = "Tea"
```

## 📊 Tableau Interactive Dashboard

👉 Live Dashboard on Tableau Public:
🔗 Click to view the full interactive dashboard：
https://public.tableau.com/views/AustralianBeverageMarketInsightDashboard/Dashboard1




