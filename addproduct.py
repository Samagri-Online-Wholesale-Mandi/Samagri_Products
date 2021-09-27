import csv
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Samagri_Products"]
mycol = mydb["Products"]
mycol.drop()
with open('Samagri_Products.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        mydict = {"product_id":row[6],"product_type":row[0], "product": row[1],"price":int(row[3]),"measurement":row[4]}
        x = mycol.insert_one(mydict)
        