# crawler/utils.py
import random, time, requests

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
]

def get_random_headers():
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept-Language": "en-IN,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    }

def polite_sleep(min_s=1.0, max_s=3.0):
    time.sleep(random.uniform(min_s, max_s))

def safe_get(session, url, headers=None, retries=3, timeout=12):
    headers = headers or get_random_headers()
    for i in range(retries):
        try:
            r = session.get(url, headers=headers, timeout=timeout)
            if r.status_code == 200:
                return r
            if r.status_code in (429, 503):
                time.sleep(2 ** i)
            else:
                # other 4xx/5xx - return r for debugging if needed
                return r
        except requests.RequestException:
            time.sleep(1 + i)
    return None
