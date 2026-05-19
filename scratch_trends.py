import os
import sys
from main import get_etsyhunt_keyword_data

keywords = [
    "pride shirt",
    "bachelorette shirts",
    "summer vibes",
    "lake life",
    "camping mug",
    "teacher appreciation gift",
    "beach tote",
    "festival outfit",
    "bridesmaid gift",
    "graduation gift 2026"
]

print("Fetching data from EtsyHunt for upcoming trends...\n")
for kw in keywords:
    data = get_etsyhunt_keyword_data(kw)
    if data:
        print(f"Keyword: {kw}")
        print(f"  Search Volume: {data.get('search', 'N/A')}")
        print(f"  Competition: {data.get('competition', 'N/A')}")
        print(f"  Sales: {data.get('sales', 'N/A')}")
        print("-" * 40)
    else:
        print(f"Keyword: {kw} - No data returned")
        print("-" * 40)
