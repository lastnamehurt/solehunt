from django.db import models


class BlogPost(models.Model):
    """
    Internal store of a Ghost Blog
    """
    id = models.AutoField(primary_key=True)
    post_id = models.CharField(max_length=75, null=True)
    author = models.ForeignKey("subscribers.Subscriber", on_delete=models.CASCADE, null=True)
    slug = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    body = models.TextField()
    publishedAt = models.TimeField(name="timestamp")
    url = models.URLField()
    context = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=200)

    def __str__(self):
        return "{} {}".format(self.id, self.title)
