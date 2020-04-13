from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.ForeignKey(User, related_name="+", null=True, on_delete=models.CASCADE)
    twitter_id = models.CharField(max_length=75)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    bio = models.TextField()
    avatar = models.ImageField()
    isSubscribedToDigest = models.BooleanField(default=False)
    # subscriber = models.ForeignKey("subscribers.Subscriber", null=True, related_name="subscriber", on_delete=models.CASCADE)
    signupConfirmation = models.BooleanField(default=False)

    def __str__(self):
        return self.fullName()

    class Meta:
        db_table = 'profile'

    def fullName(self):
        return "{} {}".format(self.first_name, self.last_name)

# @receiver(post_save, sender=User)
# def update_profile_signal(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.save()
