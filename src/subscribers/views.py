from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics

from subscribers.models import Subscriber
from subscribers.serializers import SubscriberSerializer


class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer


def home(request):
    return render(request, "home.html")
