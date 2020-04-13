from django.contrib.auth.models import User
from rest_framework import serializers

from subscribers.models import Subscriber


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ('id', 'alias', 'isActive')


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Subscriber.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'subscribers']
