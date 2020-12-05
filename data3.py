
import requests
import csv

req = requests.get(
        'https://73f126e804bfb0d71abb22ed19bd126a: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@bigcone.myshopify.com/admin/api/2020-10/customers.json',
        'Authorization: Basic 73f126e804bfb0d71abb22ed19bd126a')
a = req.json()

# Convert to csv file and save
b = a['customers']
for data in b:
    del data['addresses']
    del data['tax_exemptions']
    del data['default_address']
column = []
for col in b[0].keys():
    column.append (col)

with open ('customer12.csv', 'w', encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=column)
    w.writeheader()
    w.writerows(b)