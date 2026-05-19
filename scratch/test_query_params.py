import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ETSYHUNT_API_KEY", "")

url = "https://api.ehunt.ai/api/v1/keyword"

params_to_test = [
    {"keyword": "funny cat shirt", "token": api_key},
    {"keyword": "funny cat shirt", "apiKey": api_key},
    {"keyword": "funny cat shirt", "key": api_key},
    {"keyword": "funny cat shirt", "api_key": api_key},
    {"keyword": "funny cat shirt", "access_token": api_key},
]

for i, params in enumerate(params_to_test):
    try:
        r = requests.get(url, params=params, timeout=10)
        print(f"Test Param combination {i}:")
        print(f"  Params keys: {list(params.keys())}")
        print(f"  Status: {r.status_code}")
        print(f"  Response: {r.text}")
        print("-" * 50)
    except Exception as e:
        print(f"Test {i} failed: {e}")
