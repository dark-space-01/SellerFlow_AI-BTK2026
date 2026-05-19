import requests

payload = {
    "niche": "Vintage Hiking Club",
    "design_style": "minimalist",
    "tag_strategy": "balanced",
    "mockup_type": "sweatshirt",
    "is_design_product": True
}

try:
    print("Sending POST request to /api/generate...")
    r = requests.post("http://127.0.0.1:8000/api/generate", json=payload, timeout=60)
    print("Status Code:", r.status_code)
    data = r.json()
    print("Status in JSON:", data.get("status"))
    print("Mockup URL:", data.get("mockup_url"))
    print("Mockup URLs List:", data.get("mockup_urls"))
    print("SEO Data Keys:", data.get("seo_data", {}).keys() if data.get("seo_data") else None)
except Exception as e:
    print("Error calling API:", e)
