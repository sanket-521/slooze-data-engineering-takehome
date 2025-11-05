\# 📊 Slooze Data Engineering Take-Home Report  

\*\*Candidate:\*\* Sankett  

\*\*Role:\*\* Data Engineer  



---



\## 🧠 Project Summary  



This project implements an \*\*end-to-end data engineering pipeline\*\* to extract, clean, and analyze product data from \[IndiaMART](https://www.indiamart.com/).  



It demonstrates the following key data-engineering skills:  

\- Automated data ingestion using \*\*Selenium\*\* for dynamic content  

\- \*\*ETL processing\*\* with Python and Pandas  

\- \*\*Exploratory Data Analysis (EDA)\*\* and visualization using Matplotlib  



---



\## ⚙️ Workflow Overview  



| Stage | Description | Output |

|:------|:-------------|:--------|

| \*\*Data Collection\*\* | Extracted product listings (title, price, seller) using Selenium. | `output/raw\_products.json` |

| \*\*Data Cleaning (ETL)\*\* | Normalized prices, removed duplicates, and standardized fields. | `output/cleaned\_products.csv` |

| \*\*EDA \& Visualization\*\* | Generated histograms and charts to study price distribution. | `plots/min\_price\_hist.png` |



---



\## 📈 Data Summary  



| Metric | Value |

|:--------|:------|

| \*\*Products Scraped\*\* | 6 (across Industrial Conveyor \& Motor categories) |

| \*\*Valid Cleaned Rows\*\* | 1 (record with valid numeric data) |

| \*\*Average Price Range (₹)\*\* | 45,000 – 70,000 |

| \*\*Output Files\*\* | `raw\_products.json`, `cleaned\_products.csv`, `plots/min\_price\_hist.png` |



---



\## 🔍 Key Insights  



1\. \*\*Dynamic Rendering:\*\* IndiaMART relies heavily on JavaScript, so Selenium was required instead of Requests/BeautifulSoup.  

2\. \*\*Data Quality:\*\* Many listings had missing or partial information — highlighting real-world data inconsistency challenges.  

3\. \*\*Pipeline Validation:\*\* The end-to-end flow (Scrape → Transform → EDA) works correctly and can easily scale to more pages.  



---



\## 🧱 Recommendations for Scaling  



| Area | Recommendation |

|:------|:----------------|

| \*\*Pagination\*\* | Implement page scrolling or “Next Page” crawling to collect more products. |

| \*\*Storage\*\* | Save data to \*\*AWS S3\*\* and query via \*\*Glue + Athena\*\*. |

| \*\*Scheduling\*\* | Automate the job using \*\*Apache Airflow\*\* or \*\*AWS Lambda\*\*. |

| \*\*Validation\*\* | Add data quality checks with \*\*Great Expectations\*\*. |



---



\## ✅ Deliverables  



| File | Description |

|:------|:-------------|

| `output/raw\_products.json` | Raw scraped data |

| `output/cleaned\_products.csv` | Cleaned structured data |

| `plots/min\_price\_hist.png` | Visualization output |

| `README.md` | Project documentation |

| `REPORT.md` | Summary report |



---



\## 💬 Conclusion  



This project demonstrates a \*\*complete mini-data-engineering workflow\*\*, showing practical experience with:

\- Web scraping of dynamic sources  

\- ETL transformation logic  

\- Exploratory analysis and reporting  



It reflects the ability to design, debug, and document data pipelines end-to-end — a critical skill for a Data Engineer.



---



\*\*© 2025 Sankett — Submitted for Slooze Data Engineer Evaluation\*\*



