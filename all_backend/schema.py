import graphene
import contact.schema
import blog.schema
import users.schema
import job.schema
import graphql_jwt


class Query(blog.schema.Query, contact.schema.Query, job.schema.Query, users.schema.Query, graphene.ObjectType):
    pass


class Mutation(blog.schema.Mutation, contact.schema.Mutation, job.schema.Mutation, users.schema.Mutation,  graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
