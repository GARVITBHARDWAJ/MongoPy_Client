from pymongo import MongoClient
client = MongoClient()
client = MongoClient("mongodb://localhost:27017/")
mydb = client.springreact
mycol = mydb.GaganCol

try: 
    conn = MongoClient() 
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB") 
mylist = [
{"Product": "Bread", "Region": "National","Province": "", "Price": 20},
{"Product": "Bread", "Region": "Province","Province": "Rajasthan", "Price": 40},
{"Product": "Butter", "Region": "National","Province": "", "Price": 30},
{"Product": "Lassi", "Region": "National","Province": "", "Price": 20},
{"Product": "Lassi", "Region": "Province","Province": "Punjab", "Price": 10},

]
x = mycol.insert_many(mylist)
    
"""cursor = mycol.find() 
for record in cursor: 
    print(record) 
"""
product = input("Enter the product name: ")
province = input("Enter the Province else keep it Empty: ")
mydoc = mycol.find(
    {
        "Product": { "$eq" : product}, "Province": { "$eq" : ""}
    }
)

mydoc_p = mycol.find(
    {
        "Product": { "$eq" : product}, "Province": { "$eq" : province}
    }
)
lis = []   
lis2 = []

if province=="":
    for x in mydoc:
        lis.append(x["Price"])
    if len(lis)==0:
        print("There is No match for such pair.")    
    else:
        print(lis)
else:
    for x in mydoc_p:
        lis2.append(x["Price"])
    if len(lis2)==0:
        print("There is No Match for such Pair in List.")
    else:    
        print(lis2)            