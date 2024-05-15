#!/usr/bin/env python3
""" function that returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """
    Retrieve a list of schools that have a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.
        topic (str): The topic to search for.

    Returns:
        pymongo.cursor.Cursor: A cursor object containing the matching schools.
    """
    query = {"topics": topic}
    return mongo_collection.find(query)
