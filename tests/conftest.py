import motor.motor_asyncio
import pytest
import os
from bson.objectid import ObjectId
from .dummy_types import loop
from datetime import datetime


@pytest.fixture(scope="session", autouse=True)
def check_environment():
    if 'MONGO_TEST_DB_URI' not in os.environ:
        raise Exception("\n\nMONGO_TEST_DB_URI "
                        "environment variable must be defined\n"
                        "eg: MONGO_TEST_DB_URI="
                        "mongodb://user:password@localhost:27017/my_test_db\n")


@pytest.fixture(scope="session")
def event_loop():
    local_loop = loop
    yield local_loop
    local_loop.close()


@pytest.fixture(scope="session")
def mongo_test_db(event_loop):
    client = motor.motor_asyncio.AsyncIOMotorClient(
        os.environ['MONGO_TEST_DB_URI'], io_loop=event_loop
    )
    return client.get_default_database()


@pytest.fixture(scope="session", autouse=True)
async def inject_test_data(check_environment, mongo_test_db):
    print("-------------------")
    print("Injecting test data")
    print("-------------------")
    await mongo_test_db.drop_collection("profiles")
    await mongo_test_db.drop_collection("friends")
    await mongo_test_db.create_collection("profiles", capped=False, size=100)
    profiles = [
        {
            '_id': ObjectId("60f0153c49c512366274ec{:02x}".format(i)),
            'first_name': f'user-{i}',
            'email': f'user-{i}@graphene-is-awesome.com'
        } for i in range(100)
    ]
    await mongo_test_db["profiles"].insert_many(profiles)

    await mongo_test_db.create_collection("friends", capped=False, size=30)
    friends = [
        {
            '_id': ObjectId("60f01a0b49c512366274ec{:02x}".format(i)),
            'user_id': ObjectId("60f0153c49c512366274ec00"),
            'friend_id': ObjectId("60f0153c49c512366274ec{:02x}".format(i)),
            'friend_since': datetime(year=2021, month=3, day=i, hour=0, minute=0, second=0, microsecond=0)
        } for i in range(1, 30)
    ]
    await mongo_test_db["friends"].insert_many(friends)
