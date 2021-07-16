import binascii
from bson.objectid import ObjectId
from graphql_relay.utils import base64, unbase64

from typing import Optional

from graphene.relay.connection import PageInfo
from graphql_relay.connection.connectiontypes import Connection, Edge

"""A type alias for cursors in this implementation."""
ConnectionCursor = str


def connection_from_mongo(data,
                          connection_type=None,
                          edge_type=None,
                          page_info_type=None,
                          ctx={}):
    """
    A simple function that use the graphQL context to retrieve the
    has_next_page and has_previous_page value
    """
    connection_type = connection_type or Connection
    edge_type = edge_type or Edge
    page_info_type = page_info_type or PageInfo

    edges = [
        edge_type(node=node, cursor=offset_to_cursor(node.id))
        for i, node in enumerate(data)
    ]

    first_edge_cursor = edges[0].cursor if edges else None
    last_edge_cursor = edges[-1].cursor if edges else None
    has_previous_page = "has_previous" in ctx and ctx["has_previous"] or False
    has_next_page = "has_next" in ctx and ctx["has_next"] or False

    result = connection_type(
        edges=edges,
        page_info=page_info_type(
            start_cursor=first_edge_cursor,
            end_cursor=last_edge_cursor,
            has_previous_page=has_previous_page,
            has_next_page=has_next_page,
        ),
    )

    return result


PREFIX = "objectId:"


def offset_to_cursor(offset: int) -> ConnectionCursor:
    """Create the cursor string from an offset."""
    return base64(f"{PREFIX}{offset}")


def cursor_to_offset(cursor: ConnectionCursor) -> Optional[ObjectId]:
    """Retrieve the offset from the cursor string."""
    try:
        return ObjectId(unbase64(cursor)[len(PREFIX):])
    except binascii.Error:
        return None


def get_offset_with_default(
        cursor: ConnectionCursor = None, default_offset=None
) -> ObjectId:
    """Get offset from a given cursor and a default.

    Given an optional cursor and a default offset, return the offset to use;
    if the cursor contains a valid offset, that will be used,
    otherwise it will be the default.
    """
    if not isinstance(cursor, str):
        return default_offset

    offset = cursor_to_offset(cursor)
    return default_offset if offset is None else offset
