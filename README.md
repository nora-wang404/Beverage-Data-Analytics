# Australian Beverage Market Data Analytics (Woolworth vs Coles vs ALDI)
## 📌 Project Overview

The Fast-Moving Consumer Goods (FMCG) market in Australia and New Zealand is highly concentrated, dominated by a ‘Duopoly-plus-One’ structure. This includes Woolworths (the market leader, focusing on full-service offerings and expansive private label brands), Coles (the primary competitor, actively pursuing digital transformation in recent years), and Aldi (the major challenger, rapidly growing due to its Everyday Lowest Price model and limited assortment strategy).


The beverage category is a high-growth, high-competition segment, encompassing high-margin sub-markets from traditional carbonated soft drinks to functional health beverages and ready-to-drink coffee. For any new market entrant, selecting the correct distribution channel is the critical determinant of its ability to break through in this saturated environment.


This project analyzes the price strategy, promotion depth, and category-level competition in the Australian grocery beverage market (Woolworths, Coles, Aldi).
This project aims to move beyond traditional qualitative market research by employing a data-driven methodology. I will quantify each channel's market entry barriers, potential profit margins, and brand alignment by comparatively analyzing the existing beverage category structure (e.g., sub-market penetration), pricing strategy, and promotional behavior patterns (e.g., discount depth, bundling strategies) across Woolworths, Coles, and Aldi. The resulting Channel Suitability Model will serve as a data-informed playbook for the new product’s market entry strategy.

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


## 🛠️ Tech Stack

Languages & Tools

Python — scraping, data cleaning (requests, pandas)

Tableau — interactive dashboards, visual analytics

R Markdown - proposal and report

Jupyter Notebook — end-to-end data processing pipeline documentation

Excel — manual verification & supplemental checks

Git & GitHub — version control & collaboration

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

Live Dashboard on Tableau Public or download beverage_analytics.twbx.

🔗 Click to view the full interactive dashboard：
https://public.tableau.com/views/AustralianBeverageMarketInsightDashboard/Dashboard1

Preview:
![Dashboard Screenshot](images_sample/Dashboard%202.png)

## ✅ Key Insights (Summery)

💚Woolworths positions strongly toward premium beverages.
With the widest SKU range and consistent high-price positioning, Woolworths is the best entry point for high-value, differentiated products. Promotions should be used selectively, leveraging Woolworths’ ability to maintain premium perception and provide strong brand exposure.

❤️Coles acts as a versatile, promotion-friendly channel for new launches.
Its broad SKU acceptance and more aggressive discounting make Coles ideal for testing market response, accelerating trial, and driving early-stage turnover—especially for value-driven or scalable products.

💙Aldi suits challenger brands offering low-cost, high-turnover SKUs.
With narrow SKU acceptance and a strict EDLP (Everyday Low Price) model, Aldi favours brands that can deliver stable supply at the lowest market price. It is not a fit for niche or premium beverages, but effective for cost-leadership entrants seeking rapid volume movement.

## 📮 Contact

If you’d like to discuss retail analytics, data processing, or dashboard design:

Author: Ruonan Wang (Nora)🐘

Email: ruonanwang.nora@outlook.com

LinkedIn: www.linkedin.com/in/ruonanhappylife

### Discussion and suggestions are always welcomed here!
### Btw, opening to work ~
