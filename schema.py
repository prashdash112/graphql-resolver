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
