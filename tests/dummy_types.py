import asyncio
import os

import graphene
import motor.motor_asyncio
from bson.objectid import ObjectId
from dotenv import load_dotenv
from graphene import relay
from graphene.types import Scalar
from graphene.types.objecttype import ObjectType
from graphql.language import ast

from graphene_mongo_async.mongo_connection import cursor_to_offset
from graphene_mongo_async.mongo_connection_query import (
    first_after,
    last_before,
)
from graphene_mongo_async.types import MongoAsyncConnectionField
from graphene_mongo_async.utils import select_fields_from_edges_and_node
from graphene_mongo_async.utils import strip_id, select_fields_from_query

load_dotenv()
loop = asyncio.new_event_loop()

client = motor.motor_asyncio.AsyncIOMotorClient(
    os.environ['MONGO_TEST_DB_URI'], io_loop=loop
)
db = client.get_default_database()


class BsonId(Scalar):
    @staticmethod
    def serialize(obj_id):
        return str(obj_id)

    @staticmethod
    def parse_literal(node):
        if isinstance(node, ast.StringValue):
            return ObjectId(node.value)

    @staticmethod
    def parse_value(value):
        return ObjectId(value)


class Profile(ObjectType):
    class Meta:
        name = "Profile"
        interfaces = (relay.Node,)

    first_name = graphene.String()
    email = graphene.String()


class Friend(ObjectType):
    class Meta:
        name = "Friend"
        interfaces = (relay.Node,)

    friend_id = BsonId(description="The friend id used for internal purpose")
    friend_since = graphene.DateTime(description="The date since we are friend")
    profile = graphene.Field(Profile, description="The profile associated to this friend")

    @staticmethod
    async def resolve_profile(friend, info, **args):
        # Not efficient at all here with normalised models.
        # If we fetch 10 results, we end up with 10 queries :)
        profile = await db["profiles"].find_one({'_id': ObjectId(friend.friend_id)})
        strip_id(profile)
        return Profile(**profile)

    @staticmethod
    async def resolve_friend_since(friend, info, **args):
        return friend.friend_since


class FriendConnection(relay.Connection):
    class Meta:
        node = Friend


class Me(Profile):
    class Meta:
        name = "Me"
        db = db
        interfaces = (relay.Node,)

    friends = MongoAsyncConnectionField(
        FriendConnection, description="Friends that I haven't seen before :)"
    )

    @staticmethod
    async def resolve_friends(me, info, **args):
        page_size = None
        last_id = None
        mongo_query = first_after

        if "first" in args:
            page_size = args["first"]
        if "after" in args:
            last_id = cursor_to_offset(args["after"])
        if "last" in args:
            page_size = args["last"]
            mongo_query = last_before
        if "before" in args:
            mongo_query = last_before
            last_id = cursor_to_offset(args["before"])

        if page_size is None:
            page_size = 10

        fields_selection = select_fields_from_edges_and_node(info)
        fields_selection["friend_id"] = 1

        # handle relay specific pagination
        result = await mongo_query(
            collection=db["friends"],
            query={'user_id': me.id},
            selection=fields_selection, page_size=page_size, last_id=last_id
        )
        info.context["has_previous"] = result.has_previous
        info.context["has_next"] = result.has_next

        end_result = []
        for doc in result.data:
            end_result.append(Friend(**doc))
        return end_result


class Query(graphene.ObjectType):
    me = graphene.Field(Me, id=graphene.String(required=True))

    @staticmethod
    async def retrieve_me(id, fields_to_query):
        return await db.profiles.find_one(
            {"_id": ObjectId(id)}, fields_to_query
        )

    @staticmethod
    async def resolve_me(root, info, *args, id, **kwargs):
        if len(info.field_asts) > 0:
            fields_to_query = select_fields_from_query(info.field_asts[0])
        else:
            fields_to_query = {}

        doc = await Query.retrieve_me(id, fields_to_query)
        strip_id(doc)
        return Me(**doc)
