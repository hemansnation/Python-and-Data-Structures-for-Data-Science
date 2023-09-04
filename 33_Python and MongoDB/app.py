from flask import Flask
import pymongo
from bson.objectid import ObjectId

MONGODB_URI = 'mongodb+srv://pythonclosed:python12345@cluster0.96mmy7a.mongodb.net/?retryWrites=true&w=majority'

client = pymongo.MongoClient(MONGODB_URI)

# create database
db = client.college

# #  collection(table)           document(rows)
# db.students.insert_one({'name':'Sunil', 'country':'India', 'city': 'indore', 'age':21})


# print(client.list_database_names())

# students = [
#     {'name':'Sunil', 'country':'India', 'city': 'indore', 'age':21},
#     {'name':'Ravi', 'country':'India', 'city': 'indore', 'age':25},
#     {'name':'Alex', 'country':'USA', 'city': 'Seatle', 'age':43},
# ]

# for s in students:
#     db.students.insert_one(s)

s = db.students.find_one({'_id':ObjectId('64f547ec2947ee9e3d7e00fc')})
print(s)

app = Flask(__name__)

if __name__ =='__main__':
    app.run(debug=True, port=5000)