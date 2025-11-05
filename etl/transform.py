# etl/transform.py
import json, re
import pandas as pd
from datetime import datetime

RAW_PATH = "output/raw_products.json"
CLEAN_PATH = "output/cleaned_products.csv"

def parse_price(price_text):
    if not price_text:
        return None, None, None
    s = price_text.replace(",", "").replace("₹", " ").replace("INR", " ").replace("Rs.", " ")
    nums = re.findall(r"\d+(?:\.\d+)?", s)
    nums = [float(n) for n in nums] if nums else []
    if not nums:
        return price_text.strip(), None, None
    if len(nums) == 1:
        return price_text.strip(), nums[0], nums[0]
    return price_text.strip(), min(nums), max(nums)

def normalize_location(loc_text):
    if not loc_text:
        return None, None
    parts = [p.strip() for p in re.split(r",|\||-", loc_text) if p.strip()]
    city = parts[0] if parts else None
    state = parts[1] if len(parts) > 1 else None
    return city, state

def load_and_clean(raw_path=RAW_PATH, clean_path=CLEAN_PATH):
    with open(raw_path, encoding="utf-8") as f:
        raw = json.load(f)
    rows = []
    for r in raw:
        price_txt = r.get("price")
        price_raw, min_price, max_price = parse_price(price_txt)
        city, state = normalize_location(r.get("seller_location") or "")
        rows.append({
            "title": r.get("title"),
            "product_url": r.get("product_url"),
            "price_raw": price_raw,
            "min_price": min_price,
            "max_price": max_price,
            "seller_name": r.get("seller_name"),
            "seller_city": city,
            "seller_state": state,
            "description": r.get("description"),
            "specs": r.get("specs"),
        })
    df = pd.DataFrame(rows)
    # basic cleaning
    df['min_price'] = pd.to_numeric(df['min_price'], errors='coerce')
    df['max_price'] = pd.to_numeric(df['max_price'], errors='coerce')
    df.drop_duplicates(subset=['product_url'], inplace=True)
    df.to_csv(clean_path, index=False)
    print("Wrote cleaned data:", clean_path, "rows:", len(df))
    return df

if __name__ == "__main__":
    load_and_clean()
