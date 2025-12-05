#!/usr/bin/env python3
"""Module that lists all documents in a MongoDB collection."""


def list_all(mongo_collection) -> list:
    """List all documents in a MongoDB collection.

    Args:
        mongo_collection: The MongoDB collection object.

    Returns:
        A list of all documents in the collection.
    """
    return list(mongo_collection.find())


if __name__ == "__main__":
    from pymongo import MongoClient
    client = MongoClient('mongodb://localhost:27017/')
    db = client.test
    collection = db.school
    documents = list_all(collection)
    for doc in documents:
        print(doc)
