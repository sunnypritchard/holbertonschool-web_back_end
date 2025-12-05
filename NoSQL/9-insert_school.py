#!/usr/bin/env python3
"""Insert a new document in a MongoDB collection based on kwargs."""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document in a MongoDB collection.

    Args:
        mongo_collection: The MongoDB collection object.
        **kwargs: Key-value pairs representing the document to insert.

    Returns:
        The ID of the inserted document.
    """
    insert_result = mongo_collection.insert(kwargs)
    return insert_result.inserted_id
