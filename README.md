# Graphene Mongo Async

A spike using [graphene](https://github.com/graphql-python/graphene) 
and mongo async library [motor](https://github.com/mongodb/motor/).
It is compatible with relay pagination and does not use any other libraries

## Setup
> Create a .env file in the root directory and append MONGO_TEST_DB_URI env variable pointing to a valid mongo database eg: <br>
> MONGO_TEST_DB_URI=mongodb://localhost:27017/test_db

## Run locally
> pytest

It works for Query but can easily be extended for Mutations and 
subscription eg: 
>  query me { <br>
>   &nbsp;&nbsp;&nbsp;&nbsp; firstName <br>
>   &nbsp;&nbsp;&nbsp;&nbsp; email <br>
>   &nbsp;&nbsp;&nbsp;&nbsp; friends(first:10, after:"60b4a7425066eda8ccad0256") { <br>
>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; edges { <br>
>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; cursor <br>
>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; node { <br>
>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; firstName <br>
>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; email <br>
>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; } <br>
>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; } <br>
>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; pageInfo { <br>
>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; hasPreviousPage <br> 
>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; hasNextPage <br>
>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; startCursor <br>
>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; endCursor <br>
>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; } <br>
>   &nbsp;&nbsp;&nbsp;&nbsp; } <br>
> }
