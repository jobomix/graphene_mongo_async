import motor.motor_asyncio
from graphene.utils.str_converters import to_snake_case
from graphql.language.ast import Field


def is_db_valid(db):
    """db must be a valid async motor database"""
    return db is not None and isinstance(
        db, motor.motor_asyncio.AsyncIOMotorDatabase
    )


def doc_to_mongo_field(root: Field):
    """Match exact set of required fields to fulfill the mongo query"""
    fields_to_query = {}
    if root.selection_set is not None:
        for field in root.selection_set.selections:
            if field.selection_set is None:
                fields_to_query[to_snake_case(field.name.value)] = 1
    return fields_to_query


def select_edges_fields(info):
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
