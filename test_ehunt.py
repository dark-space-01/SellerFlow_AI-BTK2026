import requests, json, urllib.parse

keyword = "funny cat shirt"
encoded = urllib.parse.quote(keyword)

session = requests.Session()
base_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

# Try Etsy's internal listing count API (used by their frontend)
api_endpoints = [
    f"https://www.etsy.com/api/v3/ajax/bespoke/member/search/listings?q={encoded}&limit=1",
    f"https://www.etsy.com/search/api/listings?q={encoded}&limit=1&includes[]=pagination",
    f"https://openapi.etsy.com/v3/application/listings/active?keywords={encoded}&limit=1",
]

print("Testing Etsy API endpoints...")
for url in api_endpoints:
    try:
        r = session.get(url, headers={**base_headers, "Accept": "application/json"}, timeout=10)
        print(f"\nSTATUS {r.status_code}: {url[:70]}")
        if r.status_code == 200:
            data = r.json()
            print(json.dumps(data, indent=2)[:500])
        else:
            print("  Body:", r.text[:200])
    except Exception as e:
        print(f"  ERR: {e}")

# Also try to get count from Etsy search with different user agent
print("\n\nTrying with mobile UA...")
mobile_headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}
r = session.get(f"https://www.etsy.com/search?q={encoded}", headers=mobile_headers, timeout=15)
print(f"Mobile STATUS: {r.status_code}")
if r.status_code == 200:
    import re
    count_matches = re.findall(r'([\d,]+)\s+result', r.text, re.IGNORECASE)
    print("Count matches:", count_matches[:5])
    # Check for JSON data embedded in page
    json_blocks = re.findall(r'"total_count":\s*(\d+)', r.text)
    print("Total count in JSON:", json_blocks[:5])
