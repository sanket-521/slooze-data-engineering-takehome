# 🧠 Slooze Data Engineering Take-Home Challenge  
**Candidate:** Sanket Aba Adhav

---

## 🚀 Project Overview  

This project demonstrates an **end-to-end Data Engineering workflow** that automates the process of data collection, cleaning, transformation, and exploratory data analysis (EDA) on product listings from **IndiaMART**, a popular B2B marketplace.  

It simulates a real-world data pipeline where raw, semi-structured data is ingested, transformed, and analyzed for insights — a core responsibility of a **Data Engineer**.

---

## 🧩 Key Components  

| Stage | Description | Tools / Libraries |
|:------|:-------------|:------------------|
| **1. Data Collection** | Scrapes product information (title, price, seller, etc.) from IndiaMART using Selenium to handle JavaScript-rendered content. | Selenium, WebDriver Manager |
| **2. Data Transformation (ETL)** | Cleans and normalizes the scraped data, extracts numeric price ranges, and saves a structured dataset. | Python, Pandas, Regex |
| **3. Exploratory Data Analysis (EDA)** | Generates simple visual insights (price distribution, seller patterns) from the cleaned data. | Matplotlib, Pandas |

---

## ⚙️ Tech Stack  

- **Language:** Python 3.x  
- **Libraries:** Selenium, Pandas, Matplotlib, WebDriver-Manager  
- **Environment:** Windows PowerShell with Virtual Environment (`venv`)  
- **Output Formats:** JSON, CSV, PNG  

---

## 📂 Project Structure  

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


---

## 🧭 How to Run the Project  

### 1️⃣ Create and Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\Activate.ps1

### 2️⃣ Install Dependencies
pip install -r requirements.txt

### 3️⃣ Run the Complete Pipeline
# Step 1: Scrape data from IndiaMART
python crawler\scraper_selenium.py

# Step 2: Transform & clean data
python etl\transform.py

# Step 3: Generate EDA plots
python notebooks\EDA.py

### ✅ Outputs:

Raw scraped data → output/raw_products.json
Cleaned dataset → output/cleaned_products.csv
Charts → plots/min_price_hist.png, plots/top_seller_cities.png

### 🧠 Insights & Learnings

IndiaMART pages use JavaScript rendering, which made Selenium essential for data extraction.
ETL pipeline successfully cleaned inconsistent prices and normalized text data.
EDA shows that most industrial equipment lies in a mid-price range, but more records would reveal broader patterns.
Demonstrated how raw, unstructured web data can be transformed into analytics-ready datasets.

### 🧱 Future Enhancements

Pagination: Extend scraper to multiple pages per category.
Data Storage: Push cleaned data to AWS S3 and catalog via Glue + Athena.
Automation: Schedule periodic runs using Apache Airflow or AWS Lambda.
Data Validation: Add schema checks (Great Expectations / PyDeequ).
Scalability: Move pipeline to Spark for large-scale crawling.

### 📦 Submission Details

Role: Data Engineer
Organization: Slooze
Deliverables:
raw_products.json
cleaned_products.csv
EDA visualizations
REPORT.md
README.md
Submitted by: Sanket Aba Adhav

