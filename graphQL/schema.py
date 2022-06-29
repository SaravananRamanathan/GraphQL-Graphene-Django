import graphene

import api.schema

class Query(api.schema.Query, graphene.ObjectType):
    ""

class Mutation(api.schema.Mutation,graphene.ObjectType):
    ""

#schema = graphene.Schema(query=Query)
schema = graphene.Schema(query=Query,mutation=Mutation)