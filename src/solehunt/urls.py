from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import include, path
from rest_framework import routers, serializers, viewsets

from accounts.views import (activate, activation_sent_view, home_view,
                            signup_view)
# Serializers define the API representation.
from subscribers.views import SubscriberViewSet


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'subscribers', SubscriberViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('home', home_view, name="home"),
    path('signup/', signup_view, name="signup"),
    path('sent/', activation_sent_view, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name="activate"),
    # imported urls
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('custom_api/', include('subscribers.urls')),
]
