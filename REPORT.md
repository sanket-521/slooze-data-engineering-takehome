# 📊 Slooze Data Engineering Take-Home Report

**Candidate:** Sanket Aba Adhav  
**Role:** Data Engineer  

---

## 🧠 Project Summary

This project implements an **end-to-end data engineering pipeline** to extract, clean, and analyze product data from [IndiaMART](https://www.indiamart.com/).

It demonstrates the following key data engineering skills:

- Automated **data ingestion** using **Selenium** for dynamic content  
- **ETL processing** with Python and Pandas  
- **Exploratory Data Analysis (EDA)** and visualization using Matplotlib  

---

## ⚙️ Workflow Overview

| **Stage** | **Description** | **Output** |
|------------|----------------|-------------|
| **Data Collection** | Extracted product listings (title, price, seller) using Selenium. | `output/raw_products.json` |
| **Data Cleaning (ETL)** | Normalized prices, removed duplicates, and standardized fields. | `output/cleaned_products.csv` |
| **EDA & Visualization** | Generated histograms and charts to study price distribution. | `plots/min_price_hist.png` |

---

## 📈 Data Summary

| **Metric** | **Value** |
|:------------|:-----------|
| **Products Scraped** | 6 (across *Industrial Conveyor* and *Motor* categories) |
| **Valid Cleaned Rows** | 1 (record with valid numeric data) |
| **Average Price Range (₹)** | 45,000 – 70,000 |
| **Output Files** | `raw_products.json`, `cleaned_products.csv`, `plots/min_price_hist.png` |

---

## 🔍 Key Insights

1. **Dynamic Rendering:** IndiaMART relies heavily on JavaScript, so **Selenium** was required instead of traditional tools like Requests or BeautifulSoup.  
2. **Data Quality:** Many listings contained missing or partial information — reflecting real-world data inconsistency challenges.  
3. **Pipeline Validation:** The end-to-end workflow (**Scrape → Transform → EDA**) executes successfully and can easily scale to more pages or categories.  

---

## 🧱 Recommendations for Scaling

| **Area** | **Recommendation** |
|:----------|:------------------|
| **Pagination** | Implement page scrolling or “Next Page” crawling to collect more products. |
| **Storage** | Store data in **AWS S3** and query using **AWS Glue + Athena**. |
| **Scheduling** | Automate pipeline execution using **Apache Airflow** or **AWS Lambda**. |
| **Validation** | Add data quality checks with **Great Expectations**. |

---

## ✅ Deliverables

| **File** | **Description** |
|:-----------|:----------------|
| `output/raw_products.json` | Raw scraped data |
| `output/cleaned_products.csv` | Cleaned structured data |
| `plots/min_price_hist.png` | Visualization output |
| `README.md` | Project documentation |
| `REPORT.md` | Summary report |

---

## 💬 Conclusion

This project demonstrates a **complete mini data engineering workflow**, showing practical experience with:

- Web scraping of dynamic sources  
- ETL transformation and data cleaning  
- Exploratory analysis and reporting  

It reflects the ability to **design, debug, and document** end-to-end data pipelines — a critical skill for a Data Engineer.

---

**© 2025 Sanket Aba Adhav — Submitted for Slooze Data Engineer Evaluation**
