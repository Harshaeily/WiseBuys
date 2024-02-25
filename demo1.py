import csv
from bs4 import BeautifulSoup

# Read eBay.html
with open("eBay.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Parse HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find all divs with class="s-item__wrapper clearfix"
item_divs = soup.find_all("div", class_="s-item__wrapper clearfix")

# Write scraped data to CSV file
with open('eBay_data.csv', mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write headers
    writer.writerow(["Product Name", "Product Price", "Product Reviews"])
    
    # Loop through item divs and extract data
    for div in item_divs:
        # Initialize variables
        Product_Name = ""
        Product_Price = ""
        Product_Reviews = ""

        # Find span with class="clipped" for Product_Name
        span_name = div.find("div", class_="s-item__title")
        if span_name:
            Product_Name = span_name.text.strip()

        # Find span with class="s-item__price" for Product_Price
        span_price = div.find("span", class_="s-item__price")
        if span_price:
            Product_Price = span_price.text.strip()

        # Find span with class="s-item__reviews-count" for Product_Reviews
        span_reviews = div.find("span", class_="s-item__reviews-count")
        if span_reviews:
            Product_Reviews = span_reviews.text.strip()

        # Write data to CSV file
        writer.writerow([Product_Name, Product_Price, Product_Reviews])
