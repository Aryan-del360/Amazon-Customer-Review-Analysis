import json
import csv

# File paths
input_file = 'reviews_Electronics_5.json'
output_file = 'Amazon_CX_Data.csv'

# Open JSON Lines & CSV file
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)

    # Write header row
    writer.writerow(['Customer_ID', 'Product_ID', 'Feedback_Text', 'CSAT_Score', 'Review_Date', 'Feedback_Title'])

    # Loop through each JSON line, up to 100,000 rows
    for i, line in enumerate(infile):
        if i >= 100000:
            break
        review = json.loads(line)
        writer.writerow([
            review.get('reviewerID', ''),
            review.get('asin', ''),
            review.get('reviewText', '').replace('\n', ' '),
            review.get('overall', ''),
            review.get('reviewTime', ''),
            review.get('summary', '')
        ])

print("✅ CSV created: Amazon_CX_Data.csv")
