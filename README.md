<div align="center">

# 🚀 Slooze Data Engineering Take-Home Challenge

**End-to-End Data Pipeline: Web Scraping → ETL → EDA**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Selenium](https://img.shields.io/badge/Selenium-WebScraping-success?logo=selenium)
![Pandas](https://img.shields.io/badge/Pandas-DataCleaning-lightgrey?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?logo=plotly)
![AWS](https://img.shields.io/badge/AWS-Ready-yellow?logo=amazon-aws)

</div>

---

## 📖 **Overview**

This project is an **end-to-end data engineering solution** created for the **Slooze Data Engineer assessment**.
It demonstrates skills in:

* Dynamic data extraction using Selenium
* ETL pipeline design and data cleaning
* Exploratory Data Analysis (EDA) and visualization
* Building modular, scalable data workflows

---

## 🧩 **Key Features**

✅ Dynamic data extraction using **Selenium**
✅ Data cleaning and transformation via **Pandas (ETL)**
✅ EDA & visualization with **Matplotlib**
✅ Modular, reproducible folder structure
✅ Ready for scaling to **AWS S3 / Glue / Airflow**

---

## 🗂 **Project Structure**

```bash
slz_takehome/
│
├── crawler/                         # Data collection layer
│   ├── scraper_selenium.py          # Web scraper using Selenium
│   ├── utils.py                     # Helper functions (headers, safe requests)
│   └── run_crawler.py               # Entry point for crawler
│
├── etl/                             # Data cleaning and transformation layer
│   └── transform.py                 # ETL script for data normalization
│
├── notebooks/                       # Data analysis and visualization
│   └── EDA.py                       # EDA and visualization script
│
├── output/                          # Data outputs
│   ├── raw_products.json            # Raw scraped data
│   └── cleaned_products.csv         # Transformed structured dataset
│
├── plots/                           # Visualization outputs
│   ├── min_price_hist.png           # Price distribution visualization
│   └── top_seller_cities.png        # Seller city frequency chart
│
├── README.md                        # Main project documentation (this file)
├── REPORT.md                        # Summary report and insights
└── requirements.txt                 # Python dependencies
```

---

## 🧬 **How to Run the Project**

---

### 🪄 **1️⃣ Create and Activate Virtual Environment**

```bash
# Create a virtual environment
python -m venv venv

# Activate it (Windows PowerShell)
venv\Scripts\Activate.ps1
```

---

### ⚙️ **2️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

---

### 🚀 **3️⃣ Run the Complete Pipeline**

#### 🔸 Step 1: Scrape Data from IndiaMART

```bash
python crawler\scraper_selenium.py
```

#### 🗝 Step 2: Transform & Clean Data

```bash
python etl\transform.py
```

#### 📊 Step 3: Generate EDA Plots

```bash
python notebooks\EDA.py
```

---

### ✅ **Outputs**

| Type                | Description                   | File Path                                                 |
| ------------------- | ----------------------------- | --------------------------------------------------------- |
| 📥 Raw scraped data | Extracted data from IndiaMART | `output/raw_products.json`                                |
| 🯼 Cleaned dataset  | Transformed & normalized data | `output/cleaned_products.csv`                             |
| 📈 Charts           | Price & seller insights       | `plots/min_price_hist.png`, `plots/top_seller_cities.png` |

---

## 🧬 **Insights & Learnings**

* IndiaMART relies heavily on **JavaScript rendering**, requiring **Selenium** instead of static scraping.
* The **ETL pipeline** cleaned inconsistent and incomplete product data.
* EDA revealed **common price ranges and supplier concentration** across cities.
* Demonstrates how unstructured marketplace data can be turned into analytics-ready datasets.

---

## 🧱 **Future Enhancements**

| Area            | Enhancement                                                 |
| --------------- | ----------------------------------------------------------- |
| 🔄 Pagination   | Handle multiple search pages for broader coverage           |
| ☁️ Data Storage | Store cleaned data in **AWS S3**, query via **Athena/Glue** |
| 🕒 Automation   | Schedule runs via **Apache Airflow** or **AWS Lambda**      |
| ✅ Validation    | Add data quality checks with **Great Expectations**         |
| ⚡ Scalability   | Migrate ETL to **PySpark** for larger-scale processing      |

---

## 📦 **Submission Details**

| Field                  | Information                                                                               |
| ---------------------- | ----------------------------------------------------------------------------------------- |
| 🤩 **Role**            | Data Engineer                                                                             |
| 🏢 **Organization**    | Slooze                                                                                    |
| 📚 **Deliverables**    | `raw_products.json`, `cleaned_products.csv`, EDA visualizations, `REPORT.md`, `README.md` |
| 👨‍💻 **Submitted by** | **Sanket Aba Adhav**                                                                      |

---

<div align="center">

✨ *“Turning raw web data into meaningful insights — one pipeline at a time.”* ✨
**© 2025 Sanket Aba Adhav — For Slooze Data Engineer Take-Home Challenge**

</div>
