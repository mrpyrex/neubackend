import graphene
from graphene_django import DjangoObjectType
from .models import Job


class JobType(DjangoObjectType):
    class Meta:
        model = Job


class Query(graphene.ObjectType):
    jobs = graphene.List(JobType)

    job = graphene.Field(JobType,
                         id=graphene.Int(),
                         )

    def resolve_jobs(self, info):

        return Job.objects.all()

    def resolve_job(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Job.objects.get(pk=id)

        return None


class CreateJob(graphene.Mutation):
    job = graphene.Field(JobType)

    class Arguments:
        title = graphene.String()
        desciption = graphene.String()
        thumb = graphene.String()
        link = graphene.String()
        customer = graphene.String()

    def mutate(self, info, **kwargs):
        job = Job(**kwargs, author=author)
        job.save()
        return CreateJob(job=job)


class Mutation(graphene.ObjectType):
    create_job = CreateJob.Field()
