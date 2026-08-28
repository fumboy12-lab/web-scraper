import os
from bs4 import BeautifulSoup
import pandas as pd
import requests

print("[+] Initializing Web Scraper...")
url = "http://books.toscrape.com/"

response = requests.get(url)
if response.status_code == 200:
    print("[+] Successfully connected to target site.")
    soup = BeautifulSoup(response.text, "html.parser")

    books = []
    articles = soup.find_all("article", class_="product_pod")

    for item in articles:
        title = item.h3.a["title"]
        price = item.find("p", class_="price_color").text
        availability = item.find("p", class_="instock availability").text.strip()

        books.append(
            {"Title": title, "Price": price, "Availability": availability}
        )

    # Convert to DataFrame
    df = pd.DataFrame(books)

    # Export to CSV and Excel
    df.to_csv("scraped_products.csv", index=False)
    df.to_excel("scraped_products.xlsx", index=False)

    print(
        f"[+] Extraction Complete: {len(books)} items harvested successfully."
    )
    print("[+] Files saved: scraped_products.csv & scraped_products.xlsx")
else:
    print("[-] Failed to retrieve page.")