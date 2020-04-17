from django.db import models


# Create your models here.
class Post(models.Model):
    """
    A Post is an internal posting (similar to blog)
    """
    subscriber = models.ForeignKey('subscribers.Subscriber', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    body = models.TextField()
    timestamp = models.TimeField(auto_now_add=True)

    @property
    def likes(self):
        return Like.objects.filter(post_id=self.id)


class Like(models.Model):
    subscriber = models.ForeignKey('subscribers.Subscriber', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='+', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
