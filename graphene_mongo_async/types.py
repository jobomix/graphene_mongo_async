from collections import Iterable
from functools import partial

from graphene import String, Int
from graphene.relay.connection import Connection
from graphene.relay.connection import PageInfo
from graphene.relay.node import is_node
from graphene.types import NonNull
from graphene.types.field import Field
from graphene.types.objecttype import ObjectType, ObjectTypeOptions
from graphene.utils.thenables import maybe_thenable
from .mongo_connection import connection_from_mongo
from .utils import is_db_valid


class MongoAsyncObjectTypeOptions(ObjectTypeOptions):
    collection = None
    db = None


class MongoAsyncObjectType(ObjectType):
    @classmethod
    def __init_subclass_with_meta__(
            cls,
            collection=None,
            db=None,
            include=None,
            exclude=None,
            interfaces=(),
            possible_types=(),
            default_resolver=None,
            _meta=None,
            **options,
    ):
        if _meta:
            assert isinstance(_meta, MongoAsyncObjectTypeOptions), (
                "_meta must be an instance of MongoAsyncObjectTypeOptions, "
                "received {}"
            ).format(_meta.__class__)
        else:
            _meta = MongoAsyncObjectTypeOptions(cls)

        assert is_db_valid(
            db
        ), "db must be set and be a valid motor AsyncIO database instance"

        _meta.collection = collection
        _meta.db = db

        super(MongoAsyncObjectType, cls).__init_subclass_with_meta__(
            _meta=_meta, interfaces=interfaces, **options
        )


class MongoAsyncConnectionField(Field):
    def __init__(self, type, *args, **kwargs):
        kwargs.setdefault("before", String())
        kwargs.setdefault("after", String())
        kwargs.setdefault("first", Int())
        kwargs.setdefault("last", Int())
        super(MongoAsyncConnectionField, self).__init__(type, *args, **kwargs)

    @property
    def type(self):
        type = super(MongoAsyncConnectionField, self).type
        connection_type = type
        if isinstance(type, NonNull):
            connection_type = type.of_type

        if is_node(connection_type):
            raise Exception(
                "ConnectionFields now need a explicit ConnectionType for Nodes.\n"
                "Read more: https://github.com/graphql-python/graphene/blob/v2.0.0/UPGRADE-v2.0.md#node-connections"
            )

        assert issubclass(connection_type, Connection), (
            '{} type have to be a subclass of Connection. Received "{}".'
        ).format(self.__class__.__name__, connection_type)
        return type

    @classmethod
    def resolve_connection(cls, connection_type, args, info, resolved):
        if isinstance(resolved, connection_type):
            return resolved

        assert isinstance(resolved, Iterable), (
            "Resolved value from the connection field have to be iterable or instance of {}. "
            'Received "{}"'
        ).format(connection_type, resolved)
        connection = connection_from_mongo(
            resolved,
            connection_type=connection_type,
            edge_type=connection_type.Edge,
            page_info_type=PageInfo,
            ctx=info.context,
        )
        connection.iterable = resolved
        return connection

    @classmethod
    def connection_resolver(
            cls, resolver, connection_type, root, info, **args
    ):
        resolved = resolver(root, info, **args)

        if isinstance(connection_type, NonNull):
            connection_type = connection_type.of_type

        on_resolve = partial(
            cls.resolve_connection, connection_type, args, info
        )
        return maybe_thenable(resolved, on_resolve)

    def get_resolver(self, parent_resolver):
        resolver = super(MongoAsyncConnectionField, self).get_resolver(
            parent_resolver
        )
        return partial(self.connection_resolver, resolver, self.type)
