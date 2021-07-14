import pytest
from graphene_mongo_async.mongo_connection_query import first_after, last_before
from bson.objectid import ObjectId


@pytest.mark.asyncio
async def test_find_first_10_results(mongo_test_db):
    query = {'hair_color': 'BLOND'}

    result = await first_after(mongo_test_db['user'],
                               query, {'first_name': 1, 'hair_color': 1, 'eye_color': 1},
                               page_size=10, last_id=ObjectId('5f0b17501088612058a80014'))
    print(result)


@pytest.mark.asyncio
async def test_find_last_10_results(mongo_test_db):
    query = {}

    result = await last_before(mongo_test_db['user'],
                               query, {'subject': 1, 'hair_color': 1, 'eye_color': 1},
                               page_size=10, last_id=ObjectId('5f0b17df1088612058a803d8'))
    print(result)
