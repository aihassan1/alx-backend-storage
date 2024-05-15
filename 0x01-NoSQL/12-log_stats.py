#!/usr/bin/env python3
""" script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

client = MongoClient()
db = client["logs"]
collection = db.nginx

number_of_docs = collection.count_documents({})
number_of_GET = collection.count_documents({"method": "GET"})
number_of_POST = collection.count_documents({"method": "POST"})
number_of_PUT = collection.count_documents({"method": "PUT"})
number_of_PATCH = collection.count_documents({"method": "PATCH"})
number_of_DELETE = collection.count_documents({"method": "DELETE"})
number_of_GET_PATH = collection.count_documents(
    {"path": "/status", "method": "GET"})


print(f"{number_of_docs} logs")
print("Methods:")
print(f"    method GET: {number_of_GET}")
print(f"    method POST: {number_of_POST}")
print(f"    method PUT: {number_of_PUT}")
print(f"    method PATCH: {number_of_PATCH}")
print(f"    method DELETE: {number_of_DELETE}")
print(f"{number_of_GET_PATH} status check")
