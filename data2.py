import csv
import MySQLdb

mydb= MySQLdb.connect(host="127.0.0.1",user="root",password="",database="insert_csv")

with open('customer.csv') as csv_file:
    csvfile = csv.reader(csv_file, delimiter=',')
    all_values = []
    for row in csvfile:
        a=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12])
        if a[0] == 'customerid':
            continue
        all_values.append(a)
query="INSERT INTO csv(customerid, firstname, lastname, companyname, billingaddress1, billingaddress2, city, state, postalcode, country, phonenumber, emailaddress, createddate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

mycursor=mydb.cursor()
mycursor.executemany(query, all_values)

mydb.commit()