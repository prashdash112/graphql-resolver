from ariadne import QueryType
from ariadne import MutationType
from ariadne import gql
from ariadne import make_executable_schema
from ariadne.asgi import GraphQL

from mongoengine import connect
from bson.objectid import ObjectId

type_defs = gql("""
    type Event {
        name: String
        time: String
        state: String
        attendee: String
        links: String
        category: String
        date: String
        groupname: String
    }
    input EventInput {
        name: String!
        time: String!
        state: String!
        attendee: String!
        links: String!
        category: String!
        date: String!
        groupname: String!
    }
    type Query {
        events(name: String, state: String, date: String): [Event!]
    }
    type Mutation {
        add(event: EventInput!): Boolean!
        delete(id: String!): Boolean!
    }
""")

mongo_client = connect('events', host='127.0.0.1', port=27017)

query = QueryType()
mutation = MutationType()

db = mongo_client.get_database('events')
collection = db.get_collection('event')

@query.field("events")
def resolve_events(*args, **kwargs):
    print(kwargs)
    return collection.find(kwargs if len(kwargs) > 0 else {})

@mutation.field('add')
def resolve_add(*args, **kwargs):
    event = kwargs['event']

    try:
        collection.insert(event)
        return True
    except Exception as ex:
        print(ex)
        return False

@mutation.field('delete')
def resolve_delete(*args, **kwargs):
    id = kwargs['id']

    try:
        collection.remove({
            '_id': ObjectId(id),
        })

        return True
    except Exception as ex:
        print(ex)
        return False

schema = make_executable_schema(type_defs, [query, mutation])
app = GraphQL(schema, debug=True)