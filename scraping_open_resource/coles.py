import requests
import csv
import os
import random
import time

url = "https://retialer_URL"
headers = {
    "User-Agent" : "Your user agent",
    "Accept" : "*/*",
    "Content-Type" : "your content-type",
    "Referer" : "your referer"
}
page = 1

OUT_CSV = "coles_drinks.csv"
if os.path.exists(OUT_CSV):
    os.remove(OUT_CSV)
header = ["name", "brand", "package_size", "online_price", "online_was_price", "save_percent", "cup_price", "online_special", "category"]
with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerow(header)

while page <= 31:
    rows = []
    params={"slug": "drinks", "page": page}
    r = requests.get(url, headers=headers, params=params, timeout=(5,30))
    r = r.json()
    result = r.get('pageProps',{}).get('searchResults',{}).get('results',{})
    for sku in result:
        price = sku.get('pricing',{})
        # print(price)
        rows.append({
            'name': sku.get('name',[]),
            'brand': sku.get('brand',[]),
            'package_size':sku.get('size',[]),
            'online_price':price.get('now',[]),
            'online_was_price':price.get('was',[]),
            'save_percent':price.get('savePercent',[]),
            'cup_price':price.get('comparable',[]),
            'online_special':price.get('onlineSpecial', []),
            'category':sku.get('merchandiseHeir',{}).get('category',[])
        })
    if rows:
        with open(OUT_CSV, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=header)
            w.writerows(rows)
    print(f'page-writen',page)
    page+=1
    time.sleep(random.uniform(5, 10))
