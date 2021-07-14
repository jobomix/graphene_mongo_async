import asyncio

import graphene
import motor.motor_asyncio
from bson.objectid import ObjectId
from graphene import relay
from graphene.types import Scalar
from graphql.language import ast
from graphene.types.objecttype import ObjectType
from graphene_mongo_async.mongo_connection import cursor_to_offset
from graphene_mongo_async.mongo_connection_query import first_after, last_before
from graphene_mongo_async.utils import doc_to_mongo_field, select_edges_fields
from graphene_mongo_async.types import MongoAsyncConnectionField

loop = asyncio.new_event_loop()
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://nonos:secret@localhost:27017/nonoslist',
                                                io_loop=loop)
db = client['nonoslist']


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

    subject = graphene.String()
    first_name = graphene.String()
    email = graphene.String()
    description = graphene.String()
    height = graphene.Int()


class ProfileConnection(relay.Connection):
    class Meta:
        node = Profile


class Me(Profile):
    class Meta:
        name = "Me"
        db = db
        interfaces = (relay.Node,)

    non_seen_profiles = MongoAsyncConnectionField(ProfileConnection, description="People that I ve never seen before")

    @staticmethod
    async def resolve_non_seen_profiles(parent, info, **args):
        page_size = None
        last_id = None
        mongo_query = first_after

        if 'first' in args:
            page_size = args['first']
        if 'after' in args:
            last_id = cursor_to_offset(args['after'])
        if 'last' in args:
            page_size = args['last']
            mongo_query = last_before
        if 'before' in args:
            mongo_query = last_before
            last_id = cursor_to_offset(args['before'])

        if page_size is None:
            page_size = 10

        filter = select_edges_fields(info)
        result = await mongo_query(db['user'], {}, filter, page_size=page_size, last_id=last_id)
        info.context['has_previous'] = result.has_previous
        info.context['has_next'] = result.has_next
        return [Profile(**dic) for dic in result.data]
