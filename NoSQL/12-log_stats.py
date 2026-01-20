#!/usr/bin/env python3
"""Module for logging stats"""
from pymongo import MongoClient

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    # total logs
    total = collection.count_documents({})
    print(f"{total} logs")

    # methods
    print("Methods:")
    for method in METHODS:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # status check
    status_check = collection.count_documents({"path": "/status"})
    print(f"{status_check} status check")
