# crawler/run_crawler.py
from scraper_requests import run_crawl

if __name__ == "__main__":
    # pages_per_search=1 or 2 for assessment; keep small to avoid rate limits
    run_crawl(output_path="output/raw_products.json", pages_per_search=1)

