from django.shortcuts import render
from rest_framework import viewsets

from subscribers.models import Subscriber
from subscribers.serializers import SubscriberSerializer


# Create your views here.
def home(request):
    return render(request, "home.html")


class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
