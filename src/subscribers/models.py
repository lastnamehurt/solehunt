from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import Profile

class Subscriber(models.Model):
    """
    Every User is a Subscriber
    """
    id = models.AutoField(primary_key=True)
    alias = models.CharField(max_length=100)
    isActive = models.BooleanField(default=False)
    account = models.ForeignKey(Profile, related_name='+', on_delete=models.CASCADE)



    class Meta:
        db_table = 'subscriber'
        # TODO: churt expand on this implementation
        permissions = [
            (
                "can_view_sneakers", "Can View Sneakers"
            )
        ]

    def __str__(self):
        return self.alias or "N/A"


@receiver(post_save, sender=Profile)
def createSubscriber(sender, instance, created, **kwargs):
    if created:
        subscriber = Subscriber.objects.create(account=instance)
        subscriber.isActive = True
        subscriber.alias = instance.user.username
        subscriber.save()
