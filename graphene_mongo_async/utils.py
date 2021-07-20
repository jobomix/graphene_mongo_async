import motor.motor_asyncio
from graphene.utils.str_converters import to_snake_case
from graphql.language.ast import Field


def is_db_valid(db):
    """db must be a valid async motor database"""
    return db is not None and isinstance(
        db, motor.motor_asyncio.AsyncIOMotorDatabase
    )


def select_fields_from_query(root: Field):
    """Match exact set of required fields to fulfill the mongo query"""
    fields_to_query = {}
    if root.selection_set is not None:
        for field in root.selection_set.selections:
            if field.selection_set is None:
                fields_to_query[to_snake_case(field.name.value)] = 1
    return fields_to_query


def select_fields_from_edges_and_node(info):
    """Match exact set of required fields to fulfill the mongo query
    inside edges and node"""
    result = {}
    for field in info.field_asts:
        for selection in field.selection_set.selections:
            if selection.name.value == "edges":
                for edge in selection.selection_set.selections:
                    if edge.name.value == "node":
                        for f in edge.selection_set.selections:
                            if f != "id":
                                result[to_snake_case(f.name.value)] = 1
    return result


def strip_id(doc):
    if "_id" in doc:
        doc["id"] = doc["_id"]
        del doc["_id"]


# def mongo_async_relay_paginate(func):
#
#     def wrapper(root, info, args, **kwargs):
#         page_size = None
#         last_id = None
#         mongo_query = first_after
#
#         if "first" in args:
#             page_size = args["first"]
#         if "after" in args:
#             last_id = cursor_to_offset(args["after"])
#         if "last" in args:
#             page_size = args["last"]
#             mongo_query = last_before
#         if "before" in args:
#             mongo_query = last_before
#             last_id = cursor_to_offset(args["before"])
#
#         if page_size is None:
#             page_size = 10
#
#         fields_selection = select_fields_from_edges_and_node(info)
#         fields_selection["friend_id"] = 1
#
#         # # handle relay specific pagination
#         # result = await mongo_query(
#         #     collection=db["friends"],
#         #     query={'user_id': root.id},
#         #     selection=fields_selection, page_size=page_size, last_id=last_id
#         # )
#         # info.context["has_previous"] = result.has_previous
#         # info.context["has_next"] = result.has_next
#         #
#         # end_result = []
#         # for doc in result.data:
#         #     end_result.append(Friend(**doc))
#         # return end_result
#
#     return wrapper
