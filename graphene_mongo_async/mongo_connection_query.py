import pymongo
from .utils import strip_id


class AsyncMongoQueryResult:
    def __init__(self, data, last_id, has_next, has_previous):
        self.data = data
        self.last_id = last_id
        self.has_next = has_next
        self.has_previous = has_previous

    def __repr__(self):
        return str(
            {
                "data": self.data,
                "last_id": self.last_id,
                "has_next": self.has_next,
                "has_previous": self.has_previous,
            }
        )


async def first_after(
        collection, query: dict, selection: dict, page_size, last_id=None
):
    """Handle first n elements after a specific cursor.
       It has some overhead, it queries n + 2 elements to compute the
       has previous page and the has next page booleans.
    """
    has_previous = None

    if last_id is None:
        cursor = collection.find(query, selection).limit(page_size + 2)
        has_previous = False
    else:
        query.update({"_id": {"$gte": last_id}})
        cursor = collection.find(query, selection).limit(page_size + 2)

    data = []
    async for doc in cursor:
        strip_id(doc)
        data.append(doc)

    has_next = len(data[1:]) > page_size

    if has_previous is None:
        if len(data) > 0 and data[0]["id"] == last_id:
            has_previous = True
            data = data[1:]
    else:
        data = data[:-1]

    if has_next:
        data = data[:-1]

    if not data:
        return AsyncMongoQueryResult(
            data=[], last_id=None, has_previous=False, has_next=False
        )

    last_id = data[-1]["id"]
    if has_previous is None:
        has_previous = False

    if has_next is None:
        has_next = False

    return AsyncMongoQueryResult(
        data=data,
        last_id=last_id,
        has_next=has_next,
        has_previous=has_previous,
    )


async def last_before(
        collection, query: dict, selection: dict, page_size, last_id=None
):
    """Handle the query last n element before a specific cursor
   It has some overhead, it queries n + 2 elements to compute the
   has previous page and the has next page booleans.
   """
    has_next = None

    if last_id is None:
        cursor = (
            collection.find(query, selection)
                .sort("_id", pymongo.DESCENDING)
                .limit(page_size + 2)
        )
        has_previous = False
    else:
        query.update({"_id": {"$lte": last_id}})
        cursor = (
            collection.find(query, selection)
                .sort("_id", pymongo.DESCENDING)
                .limit(page_size + 2)
        )

    data = []
    async for doc in cursor:
        strip_id(doc)
        data.append(doc)

    has_previous = len(data[1:]) > page_size

    if has_next is None:
        if len(data) > 0 and data[0]["id"] == last_id:
            has_next = True
            data = data[1:]
    else:
        data = data[:-1]

    if has_previous:
        data = data[:-1]

    if not data:
        return AsyncMongoQueryResult(
            data=[], last_id=None, has_previous=False, has_next=False
        )

    last_id = data[-1]["id"]
    if has_next is None:
        has_next = False

    if has_previous is None:
        has_previous = False

    return AsyncMongoQueryResult(
        data=data,
        last_id=last_id,
        has_next=has_next,
        has_previous=has_previous,
    )
