import graphene
import pytest
from graphene.test import Client

from . import dummy_types


@pytest.mark.asyncio
async def test_friends_query_retrieves_first_10_results(mongo_test_db, snapshot):
    query = """
        query relayQuery {
            me(id:"60f0153c49c512366274ec00") {
                id
                firstName
                email
                friends(first:10) {
                    edges {
                      cursor
                      node {
                        friendSince
                        profile {
                            id
                            firstName
                            email
                        }
                      }
                    }
                }
            }
        }
    """
    schema = graphene.Schema(query=dummy_types.Query)
    client = Client(schema)
    result = await client.execute(
        query, return_promise=True, context={"request": None}
    )
    snapshot.assert_match(result)


@pytest.mark.asyncio
async def test_friends_query_display_page_info(mongo_test_db, snapshot):
    query = """
        query relayQuery {
            me(id:"60f0153c49c512366274ec00") {
                id
                firstName
                email
                friends(first:10, after:"b2JqZWN0SWQ6NjBmMDFhMGI0OWM1MTIzNjYyNzRlYzA1") {
                    edges {
                      cursor
                      node {
                        friendSince
                        profile {
                            id
                            firstName
                            email
                        }
                      }
                    }
                    pageInfo {
                        hasNextPage
                        hasPreviousPage
                        startCursor
                        endCursor
                    }
                }
            }
        }
    """
    schema = graphene.Schema(query=dummy_types.Query)
    client = Client(schema)
    result = await client.execute(
        query, return_promise=True, context={"request": None}
    )
    snapshot.assert_match(result)


@pytest.mark.asyncio
async def test_find_last_5(mongo_test_db, snapshot):
    query = """
        query relayQuery {
            me(id:"60f0153c49c512366274ec00") {
                id
                firstName
                email
                friends(last:10, after:"b2JqZWN0SWQ6NjBmMDFhMGI0OWM1MTIzNjYyNzRlYzA1") {
                    edges {
                      cursor
                      node {
                        friendSince
                        profile {
                            id
                            firstName
                            email
                        }
                      }
                    }
                    pageInfo {
                        hasNextPage
                        hasPreviousPage
                        startCursor
                        endCursor
                    }
                }
            }
        }
    """
    schema = graphene.Schema(query=dummy_types.Query)
    client = Client(schema)
    result = await client.execute(
        query, return_promise=True, context={"request": None}
    )
    snapshot.assert_match(result)
