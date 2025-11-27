import requests
import csv
import os


url = 'https://retialer_url'

headers = {
    "User-Agent": 'Your User-Agent',
    "Origin": "Your origin",
    "Accept": "Your accept"
}
payload = {
    "urrency" : "AUD",
    "serviceType" : "walk-in",
    "categoryKey" : "1000000000",
    "limit" : 30,
    "offset" :0,                  # Page_control is here: limit + offset
    "sort" : "relevance",
    "testVariant": "A",
    "servicePoint" :"G520"
}

offset = 0
max_page = 10 # the max page number on website is 6
i = 0
rows = []

for i in range(max_page):
    params = dict(payload, offset = offset)      # renew page number

    r = requests.get(url, headers=headers, params=params, timeout=(5, 30))
    r = r.json()
    items = r.get('data', [])

    for sku in items:
        name = sku.get('name', [])
        brand = sku.get('brandName', [])
        package_size = sku.get('sellingSize', [])

        price = sku.get('price', [])  # price is in inner layer
        instore_was_price = price.get('amount', [])
        instore_price = price.get('amountRelevant', [])
        instore_cup_price = price.get('comparisonDisplay', [])

        category = sku.get('categories',[])[1].get('name','')

        rows.append({
            "name": name,
            "brand": brand,
            "instore_price": instore_price,
            "instore_was_price": instore_was_price,
            "instore_cup_price": instore_cup_price,
            "package_size": package_size,
            "category":category
        })

    offset += 30   # flip page

OUT_CSV = "Aldi_drinks.csv"
if os.path.exists(OUT_CSV):
    os.remove(OUT_CSV)

header = ["name", "brand", "instore_price", "instore_was_price", "instore_cup_price", "package_size","category"]
with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerow(header)
if rows:
    with open(OUT_CSV, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=header)
        w.writerows(rows)


