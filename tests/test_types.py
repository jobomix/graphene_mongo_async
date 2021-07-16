import pytest

from graphene_mongo_async.types import MongoAsyncObjectType


def test_fail_when_db_is_not_set():
    with pytest.raises(AssertionError) as e:
        class Something(MongoAsyncObjectType):
            pass

    assert (
            "db must be set and be a valid motor AsyncIO database instance"
            == str(e.value)
    )
