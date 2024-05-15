#!/usr/bin/env python3
"""Python function that changes all topics of a
school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """Python function that changes all topics of a
    school document based on the name"""
    query = {"name": name}
    update_doc = {"$set": {"topics": topics}}
    result = mongo_collection.update_one(query, update_doc)
