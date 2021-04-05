from rest_framework import generics, viewsets
from django.shortcuts import render
from backend.models import Service, Subscriber, Organization
from backend.serializers import SubscriberSerializer, ServiceSerializer, OrganizationSerializer


class SubscriberListView(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer


class ServiceListView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class OrganizationListView(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer




