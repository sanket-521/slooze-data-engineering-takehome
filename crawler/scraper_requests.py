# crawler/scraper_requests.py
import json
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from utils import safe_get, polite_sleep, get_random_headers


BASE_HOST = "https://dir.indiamart.com"  # use dir.indiamart.com for search
# Example search endpoints you can edit:
SEARCH_URLS = [
    "https://dir.indiamart.com/search.mp?ss=industrial+conveyor",
    "https://dir.indiamart.com/search.mp?ss=industrial+motor"
]

def parse_listing_page(html, base_url=BASE_HOST):
    soup = BeautifulSoup(html, "lxml")
    items = []
    # Heuristic: find listing cards — update after manual inspection if needed
    candidates = soup.select(".resultCard, .srchL, .product-card, .list-group-item, .prdct-listing")
    if not candidates:
        # fallback: search for links that look like product links
        candidates = soup.select("a[href*='/product/'], a[href*='/detail/'], a[href*='-p']")[:50]
    for card in candidates:
        # title and url
        a = card.select_one("a[href]")
        if not a:
            continue
        href = a.get("href")
        product_url = urljoin(base_url, href)
        title = a.get_text(strip=True) or card.select_one("h2, h3, .title").get_text(strip=True) if card.select_one("h2, h3, .title") else None

        # price candidate
        price_el = card.select_one(".price, .prc, .rate") or card.select_one(".mrp, .prd-price")
        price = price_el.get_text(strip=True) if price_el else None

        seller_el = card.select_one(".company, .supplier, .seller, .company-name")
        seller = seller_el.get_text(strip=True) if seller_el else None

        items.append({
            "title": title,
            "product_url": product_url,
            "price": price,
            "seller_name": seller
        })
    return items

def parse_product_detail(html):
    soup = BeautifulSoup(html, "lxml")
    desc_el = soup.select_one(".prod-desc, .description, #product_description, .detail-desc")
    desc = desc_el.get_text(" ", strip=True) if desc_el else None

    # seller location heuristics
    loc_el = soup.select_one(".vendorLocation, .seller-location, .addr, .location")
    location = loc_el.get_text(" ", strip=True) if loc_el else None

    # specs table
    specs = {}
    # try table rows
    for tr in soup.select("table tr"):
        tds = tr.find_all(["td", "th"])
        if len(tds) >= 2:
            k = tds[0].get_text(" ", strip=True)
            v = tds[1].get_text(" ", strip=True)
            if k:
                specs[k] = v
    # fallback: dl lists
    for dl_dt, dl_dd in zip(soup.select("dt"), soup.select("dd")):
        k = dl_dt.get_text(strip=True)
        v = dl_dd.get_text(strip=True)
        if k:
            specs[k] = v

    return {"description": desc, "seller_location": location, "specs": specs}

def crawl_one_search(session, search_url, pages=1):
    results = []
    for p in range(1, pages+1):
        url = f"{search_url}&page={p}"
        resp = safe_get(session, url, headers=get_random_headers())
        if not resp or resp.status_code != 200:
            print("Failed to fetch listing page:", url, getattr(resp, "status_code", None))
            break
        listings = parse_listing_page(resp.text)
        print(f"Found {len(listings)} items on {url}")
        for item in listings:
            polite_sleep(1.0, 2.5)
            resp2 = safe_get(session, item["product_url"], headers=get_random_headers())
            if not resp2 or resp2.status_code != 200:
                print("Could not fetch detail page:", item["product_url"])
                continue
            details = parse_product_detail(resp2.text)
            record = {**item, **details}
            results.append(record)
    return results

def run_crawl(output_path="../output/raw_products.json", pages_per_search=1):
    import requests
    session = requests.Session()
    all_results = []
    for url in SEARCH_URLS:
        print("Crawling:", url)
        res = crawl_one_search(session, url, pages=pages_per_search)
        all_results.extend(res)
    # save
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)
    print("Saved", len(all_results), "records to", output_path)
    return all_results

if __name__ == "__main__":
    run_crawl()
