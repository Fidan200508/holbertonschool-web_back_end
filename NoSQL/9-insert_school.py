#!/usr/bin/env python3
"""Module for insert_school function"""


def insert_school(mongo_collection, **kwargs):
    """Function for inserting new schools"""
    return mongo_collection.insert_one(kwargs).inserted_id
