from pymongo import MongoClient
import pprint

print("Establishing connection with localhost")
#conn_id=connect()
try:
    client = MongoClient('localhost',27017)
    print("successful attempt")
except pymongo.errors.ConnectionFailure as e:
    print("couldn't connect : ", e)

databases = client.database_names()

print("Enter the name of the Database to be used : ")
print(databases)
ip= input()
#print(ip)
#create list of databases present in the client
#databases = client.database_names()
#print(databases)
index = databases.index(ip)


if (index>=0 and index<=len(databases)-1):
    #use the database
    db = client[ip]
else:
    print("Database not found")
    exit(0)

collections = db.collection_names()
print("Enter the name of the collection to be used : ")
print(collections)
ip = input()
#create list of collections present in the db
#print(db)
#collections = db.collection_names()
index = collections.index(ip)

if (index>=0 and index<=len(collections)-1):
    #use the database
    collection = db[ip]
else:
    print("Collection not found")
    exit(0)
#print(collection)
dic=collection.find_one()
#pprint.pprint(dic)

def recsrc(obj):
    field = []
    #print(obj.items())
    for key,value in obj.items():
        if isinstance(value,dict):
             temp={}
             temp[key]=recsrc(value)
             field.append(temp)
        else :
            field.append(key)
    return field
res = recsrc(dic)
print(res)

choice = 'y'

def inpt(obj) :
    row = {}
    for key in obj :
        if isinstance(key,dict) :
            for kkey, value in key.items():
                row[kkey] = inpt(value)     
        else :
            print("Enter data for %s : " %key)
            row[key] = input()
    return row
#print(inpt(res))


while( choice == 'Y' or choice == 'y'):
    collection.insert_one(inpt(res))
    print("Do you want to insert more documents ? (y=yes/ n=no) ")
    choice = input()

client.close()

