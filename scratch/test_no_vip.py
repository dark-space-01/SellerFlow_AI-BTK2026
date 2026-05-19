import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ETSYHUNT_API_KEY", "")

# Remove "vip_" prefix if present
clean_key = api_key.replace("vip_", "")

url = "https://api.ehunt.ai/api/v1/keyword"
params = {"keyword": "funny cat shirt"}

headers_to_test = [
    ("Bearer with vip_", {"Authorization": f"Bearer {api_key}"}),
    ("No prefix with vip_", {"Authorization": api_key}),
    ("Bearer clean key", {"Authorization": f"Bearer {clean_key}"}),
    ("No prefix clean key", {"Authorization": clean_key}),
]

for name, headers in headers_to_test:
    try:
        r = requests.get(url, headers=headers, params=params, timeout=10)
        print(f"Test: {name}")
        print(f"  Status: {r.status_code}")
        print(f"  Response: {r.text}")
        print("-" * 50)
    except Exception as e:
        print(f"Test: {name} failed: {e}")
