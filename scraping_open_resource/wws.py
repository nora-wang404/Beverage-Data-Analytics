import requests
import csv
import os
import time
import random
import json
import re

OUT_CSV = "woolies_drinks.csv"

url = "https://retailer_url"
headers = {
    "User-Agent":"Your user-agent",
    "Accept":"Your accept",
    "Content-Type":"Your Content-type",
    "Origin": "Your Origin",
    "Referer": "Your referer",
    "Cookie": "Your cookie"}
payload = {
    "categoryId": "1_5AF3A0A",
    "categoryVersion": "v2",
    "enableAdReRanking": False,
    "filters": [],
    "flags": {"EnableProductBoostExperiment": True},
    "formatObject": "{\"name\":\"Drinks\"}",
    "gpBoost": 0,
    "groupEdmVariants": False,
    "includeBundleItems": False,
    "isBundle": False,
    "isHideEverydayMarketProducts": False,
    "isHideUnavailableProducts": False,
    "isMobile": False,
    "isRegisteredRewardCardPromotion": False,
    "isSpecial": False,
    "location": "/shop/browse/drinks?pageNumber=1",
    "pageNumber": 1,
    "pageSize": 36,
    "sortType": "TraderRelevance",
    "url": "/shop/browse/drinks?pageNumber=1"
}


def fetch_page(n: int):
    body = dict(payload)
    body["pageNumber"] = n
    body["location"] = f"/shop/browse/drinks?pageNumber={n}"
    body["url"] = f"/shop/browse/drinks?pageNumber={n}"

    print(f"[req] pageNumber={body['pageNumber']} url={body['url']}")
    r = requests.post(url, headers=headers, json=body, timeout=(5,30))
    r.raise_for_status()    # 4xx -> error message
    return r.json()

def extract_rows(data: dict):
    bundles = data.get("Bundles", [])
    rows = []
    for bundle in bundles:
        for product in bundle.get('Products',[]):
            name = bundle.get('DisplayName', [])
            online_price = product.get('Price',[])
            online_was_price = product.get('WasPrice',[])
            instore_price = product.get('InstorePrice',[])
            instore_was_price = product.get("InstoreWasPrice",[])
            online_cup_price = product.get('CupPrice',[])
            instore_cup_price = product.get('InstoreCupPrice', [])
            cup_measure = product.get('CupMeasure',[])
            brand = product.get('Brand',[])
            package_size = product.get('PackageSize',[])
            category = product.get('AdditionalAttributes',[]).get('piescategorynamesjson',[])

            rows.append({
                "name" : name,
                "brand" : brand,
                "instore_price" : instore_price,
                "instore_was_price" : instore_was_price,
                "instore_cup_price" : instore_cup_price,
                "online_price" : online_price,
                "online_was_price" : online_was_price,
                "online_cup_price" : online_cup_price,
                "cup_measure" : cup_measure,
                "package_size" : package_size,
                "category": category
            })
    return rows

def main():
    # make CSV
    if os.path.exists(OUT_CSV):
        os.remove(OUT_CSV)

    header = ["name","brand","instore_price","instore_was_price","instore_cup_price",
              "online_price","online_was_price","online_cup_price","cup_measure","package_size","category"]
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow(header)

    page = 1
    MAX_PAGES = 100  # Webpage was 83.

    while page <= MAX_PAGES:
        data = fetch_page(page)
        rows = extract_rows(data)
        print(f"[resp] page={page} rows={len(rows)} ")
        time.sleep(random.uniform(3, 7))

        # empty data
        if not rows :
            print("hit empty page, stop.")
            break

        # write in CSV
        if rows:
            with open(OUT_CSV, "a", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=header)
                w.writerows(rows)

        page += 1

    print(f"done -> {OUT_CSV}")

if __name__ == "__main__":
    main()
