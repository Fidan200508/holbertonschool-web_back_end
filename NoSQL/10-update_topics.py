#!/usr/bin/env python3
"""Module containing functions for updating topics."""


def update_topics(mongo_collection, name, topics):
    """Updates topics in MongoDB."""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
