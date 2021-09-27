import csv
import pymongo
proddict={}
finallist=[]
with open('Samagri_Products.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        proddict[row[1]]=[row[2],row[5]]
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Samagri_Products"]
mycol = mydb["Categories"]
mycol.drop()
for i,j in proddict.items():
    mydict = {"product":i, "category": j[0],"image_url":j[1]}
    x = mycol.insert_one(mydict)