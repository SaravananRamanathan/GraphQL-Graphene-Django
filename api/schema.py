import graphene
from graphene_django import DjangoObjectType

from .models import links

#linking django models with graphQL
class LinkType(DjangoObjectType):
    class Meta:
        model = links


class Query(graphene.ObjectType):
    links = graphene.List(LinkType)

    def resolve_links(self, info, **kwargs):
        return links.objects.all()


#simple mutations
#1
class CreateLink(graphene.Mutation):
    #below are the outputs field by field --selectable they can choose what they want
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()
    rating = graphene.Int()
    #2
    class Arguments: #data's which the api will accept
        url = graphene.String()
        description = graphene.String()
        rating=graphene.Int()
    #3
    def mutate(self, info, url, description,rating):
        #saving into database part
        if rating:
            link = links(url=url, description=description,rating=rating)
        else:
            link = links(url=url, description=description)
        link.save()

        #return output to the client
        return CreateLink(
            id=link.id,
            url=link.url,
            description=link.description,
            rating=link.rating,
        )

#4
class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()