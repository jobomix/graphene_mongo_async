from graphene.types.objecttype import ObjectType, ObjectTypeOptions


class MongoAsyncObjectTypeOptions(ObjectTypeOptions):
    collection = None


class MongoAsyncObjectType(ObjectType):

    @classmethod
    def __init_subclass_with_meta__(
            cls,
            collection=None,
            include=None,
            exclude=None,
            interfaces=(),
            possible_types=(),
            default_resolver=None,
            _meta=None,
            **options
    ):
        if _meta:
            assert isinstance(_meta, MongoAsyncObjectTypeOptions), (
                "_meta must be an instance of MongoAsyncObjectTypeOptions, "
                "received {}"
            ).format(_meta.__class__)
        else:
            _meta = MongoAsyncObjectTypeOptions(cls)

        _meta.collection = collection

        super(MongoAsyncObjectType, cls).__init_subclass_with_meta__(
            _meta=_meta, interfaces=interfaces, **options
        )
