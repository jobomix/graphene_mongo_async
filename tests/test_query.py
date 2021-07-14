import pytest
import graphene
from bson.objectid import ObjectId
from graphene.test import Client
from graphene_mongo_async.utils import doc_to_mongo_field
from . import dummy_types


@pytest.mark.asyncio
async def test_profile_query(mongo_test_db):
    async def wait_for_result(id, fields_to_query):
        return await mongo_test_db.user.find_one({'_id': ObjectId(id)}, fields_to_query)

    class Query(graphene.ObjectType):
        me = graphene.Field(dummy_types.Me, id=graphene.String(required=True))

        async def resolve_me(self, info, *args, id, **kwargs):
            if len(info.field_asts) > 0:
                fields_to_query = doc_to_mongo_field(info.field_asts[0])

            doc = await wait_for_result(id, fields_to_query)
            if '_id' in doc:
                doc['id'] = doc['_id']
                del doc['_id']
            return dummy_types.Me(**doc)

    query = """
        query profileQuery {
            me(id:"60b4a7425066eda8ccad0256") {
                id
                subject
                height
                nonSeenProfiles(last: 100) {
                    edges {
                        cursor
                        node {
                            id
                            email
                            firstName
                        }
                    }
                    pageInfo {
                        hasPreviousPage
                        hasNextPage
                        startCursor
                        endCursor
                    }
                }
            }
        }
    """
    schema = graphene.Schema(query=Query)
    client = Client(schema)
    result = await client.execute(query, return_promise=True, context={"request": None})
    print(result)
