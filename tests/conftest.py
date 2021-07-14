import motor.motor_asyncio
import pytest

from .dummy_types import loop


@pytest.fixture(scope="session")
def event_loop():
    local_loop = loop
    yield local_loop
    local_loop.close()


@pytest.fixture(scope="session")
def mongo_test_db(event_loop):
    client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://nonos:secret@localhost:27017/nonoslist',
                                                    io_loop=event_loop)
    return client['nonoslist']
