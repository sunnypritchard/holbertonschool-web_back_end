#!/usr/bin/env python3
"""Update topics of school document based on the name."""


def update_topics(mongo_collection, name, topics):
    """Update topics of school document based on the name

    Args:
        mongo_collection: The MongoDB collection object.
        name: The name of the document to update.
        topics: A list of topics to set for the document.

    Returns:
        The result of the update operation.
    """
    update_result = mongo_collection.update_one(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return update_result.modified_count
