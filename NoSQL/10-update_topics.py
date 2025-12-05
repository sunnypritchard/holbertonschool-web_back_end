#!/usr/bin/env python3
"""Update topics of school document based on the name."""


def update_topics(mongo_collection, name, topics):
    """Update topics of school document based on the name."""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
