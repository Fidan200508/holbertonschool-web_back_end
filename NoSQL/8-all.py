#!/usr/bin/env python3
"""Module for list_all function"""


def list_all(mongo_collection):
    """ List all elements in a collection """
    return list(mongo_collection.find())
