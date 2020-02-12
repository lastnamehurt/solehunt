from django.contrib import admin
from subscribers.models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    pass


admin.site.register(Subscriber, SubscriberAdmin)
