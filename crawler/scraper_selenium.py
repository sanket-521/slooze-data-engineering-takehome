from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time, json, os

SEARCH_URLS = [
    "https://dir.indiamart.com/search.mp?ss=industrial+conveyor",
    "https://dir.indiamart.com/search.mp?ss=industrial+motor"
]

def scrape_indiamart():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)


    results = []

    for url in SEARCH_URLS:
        print(f"Scraping {url} ...")
        driver.get(url)
        time.sleep(4)  # allow JS to load content

        cards = driver.find_elements(By.CSS_SELECTOR, "div.product-item, div.l-cl, div.pR, div.r-cl, div.listing-card")
        if not cards:
            cards = driver.find_elements(By.CSS_SELECTOR, "div.listingCardContainer, div.mt15.mb15.w800, div.sideBarAndListing")
        print("Found cards:", len(cards))

    for c in cards[:10]:
        try:
            title = c.find_element(By.CSS_SELECTOR, "a").text
        except:
            title = None
        try:
            price = c.find_element(By.CSS_SELECTOR, ".price, .prc, .fob").text
        except:
            price = None
        try:
            seller = c.find_element(By.CSS_SELECTOR, ".company, .cmpny, .supplr-nm, .mnm-txt").text
        except:
            seller = None

        results.append({
            "title": title,
            "price": price,
            "seller": seller,
            "source_url": url
        })

    driver.quit()
    os.makedirs("output", exist_ok=True)
    with open("output/raw_products.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"✅ Scraped {len(results)} items total.")
    return results

if __name__ == "__main__":
    scrape_indiamart()
