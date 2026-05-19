import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ETSYHUNT_API_KEY", "")

url = "https://api.ehunt.ai/api/v1/keyword"
params = {"keyword": "funny cat shirt"}

headers_to_test = [
    ("Bearer prefix", {"Authorization": f"Bearer {api_key}"}),
    ("No prefix", {"Authorization": api_key}),
    ("x-api-key", {"x-api-key": api_key}),
    ("token header", {"token": api_key}),
    ("apikey header", {"apikey": api_key}),
    ("api-key header", {"api-key": api_key}),
]

for name, headers in headers_to_test:
    try:
        r = requests.get(url, headers=headers, params=params, timeout=10)
        print(f"Test: {name}")
        print(f"  Status: {r.status_code}")
        print(f"  Response: {r.text}")
        print("-" * 50)
    except Exception as e:
        print(f"Test: {name} failed with error: {e}")
