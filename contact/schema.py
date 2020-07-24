from django.conf import settings
import graphene
from django.core.mail import send_mail
from graphene_django import DjangoObjectType

from .models import Contact


class ContactType(DjangoObjectType):
    class Meta:
        model = Contact


class Query(graphene.ObjectType):
    contacts = graphene.List(ContactType)

    def resolve_contacts(self, info):

        return Contact.objects.all()


class CreateContact(graphene.Mutation):
    contact = graphene.Field(ContactType)

    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()
        enquiry = graphene.String()
        company = graphene.String()
        phone = graphene.String()
        message = graphene.String()

    def mutate(self, info, **kwargs):
        email = kwargs.get('email')
        first_name = kwargs.get('first_name')
        last_name = kwargs.get('last_name')
        enquiry = kwargs.get('enquiry')
        phone = kwargs.get('phone')
        company = kwargs.get('company')
        message = kwargs.get('message')
        recipients = ['ndifrkeumoren@gmail.com']
        send_mail('Contact Received', message, settings.EMAIL_HOST_USER,
                  recipients, fail_silently=True)
        contact = Contact(**kwargs)
        contact.save()

        return CreateContact(contact=contact)


class Mutation(graphene.ObjectType):
    create_contact = CreateContact.Field()
