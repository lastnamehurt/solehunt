from django.db import models

from blog.models import BlogPost
from posts.models import Post
from sneaker_rack.models import Sneaker


class Subscriber(models.Model):
    """
    every Subscriber maps to Profile
    once a subscription is created
    """
    id = models.AutoField(primary_key=True)
    alias = models.CharField(max_length=100)
    profile = models.ForeignKey("accounts.Profile", related_name="subscription", null=True, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=False)
    isContributor = models.BooleanField(default=False)

    @property
    def sneakers(self):
        return Sneaker.objects.filter(subscriber_id=self.id)

    @property
    def blogPosts(self):
        return BlogPost.objects.filter(subscriber_id=self.id)

    @property
    def posts(self):
        return Post.objects.filter(subscriber_id=self.id)

    class Meta:
        db_table = 'subscriber'
        app_label = 'subscribers'
        permissions = [
            ("can_view_sneakers", "Can View Sneakers"),
            ("is_contributor", "Is Contributor"),
            ("can_view_blogs", "Can View Blogs"),
        ]

    def __str__(self):
        return "{} {}".format(self.id, self.alias)

# @receiver(post_save, sender=Profile)
# def createSubscriber(sender, instance, created, **kwargs):
#     if created:
#         subscriber = Subscriber.objects.create(account=instance)
#         subscriber.isActive = True
#         subscriber.alias = instance.user.username
#         subscriber.save()
