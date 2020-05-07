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
    isActive = models.BooleanField(default=True)

    @property
    def likes(self):
        return Like.objects.filter(post_id=self.pk, isActive=True)


class Like(models.Model):
    post = models.ForeignKey('Post', related_name='+', on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    isActive = models.BooleanField(default=True)
    likedBy = models.ForeignKey('subscribers.Subscriber', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return "isActive: {}".format(self.isActive)
