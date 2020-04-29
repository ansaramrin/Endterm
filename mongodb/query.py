import pymongo
import ssl

myclient = pymongo.MongoClient("mongodb+srv://PP2:qwerty123@cluster0-nzs3u.mongodb.net/test?retryWrites=true&w=majority",ssl_cert_reqs=ssl.CERT_NONE)
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Park Lane 38" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)