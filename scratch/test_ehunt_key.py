import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ETSYHUNT_API_KEY", "")
print(f"Loaded EtsyHunt Key: {api_key[:10]}...{api_key[-5:] if len(api_key) > 5 else ''}")

if not api_key:
    print("No EtsyHunt key found in .env!")
    exit(1)

domains = [
    "https://api.ehunt.co",
    "https://api.ehunt.ai",
    "https://api.etsyhunt.com",
    "https://api.ecomscrapy.com",
    "https://api-service.ehunt.ai",
    "https://api-service.etsyhunt.com"
]

endpoints = [
    "/v1/keywords",
    "/v1/keyword/search",
    "/v1/keyword/volume",
    "/api/v1/keyword",
    "/api/v1/keywords",
    "/api/v1/search",
    "/v1/products",
]

header_templates = [
    {"Authorization": f"Bearer {api_key}"},
    {"x-api-key": api_key},
    {"Authorization": api_key},
    {"token": api_key},
    {"apikey": api_key},
    {"api-key": api_key}
]

params = {"q": "funny cat shirt", "keyword": "funny cat shirt"}

print("\nStarting Sweep of Domains and Headers...")
found_working = False

for domain in domains:
    for endpoint in endpoints:
        url = f"{domain}{endpoint}"
        for i, headers in enumerate(header_templates):
            try:
                # Try GET
                r = requests.get(url, headers=headers, params=params, timeout=5)
                if r.status_code == 200:
                    print(f"\n[SUCCESS] GET Working endpoint found!")
                    print(f"URL: {url}")
                    print(f"Header Style: {list(headers.keys())[0]}")
                    print(f"Response: {r.text[:500]}")
                    found_working = True
                    break
                elif r.status_code == 404:
                    # 404 means wrong endpoint/route, so skip other headers for this endpoint
                    break
            except Exception as e:
                pass
        if found_working:
            break
    if found_working:
        break

if not found_working:
    print("\nSweep finished. No standard GET endpoint succeeded with 200. Testing POST...")
    for domain in domains:
        for endpoint in endpoints:
            url = f"{domain}{endpoint}"
            for headers in header_templates:
                try:
                    r = requests.post(url, headers=headers, json={"keyword": "funny cat shirt"}, timeout=5)
                    if r.status_code == 200:
                        print(f"\n[SUCCESS] POST Working endpoint found!")
                        print(f"URL: {url}")
                        print(f"Header Style: {list(headers.keys())[0]}")
                        print(f"Response: {r.text[:500]}")
                        found_working = True
                        break
                except Exception:
                    pass
            if found_working:
                break
        if found_working:
            break

if not found_working:
    print("\nNo direct endpoints returned 200. Checking standard web endpoints as fallback...")
