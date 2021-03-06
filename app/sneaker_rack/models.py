from django.db import models


# Create your models here.


class Sneaker(models.Model):
    brand = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=2)
    style = models.CharField(max_length=50)
    isFavorite = models.BooleanField(default=False)
    subscriber = models.ForeignKey("subscribers.Subscriber", related_name='subscriber', null=True,
                              on_delete=models.SET_NULL)
    rack = models.ForeignKey('SneakerRack', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{} {}".format(self.brand, self.style)


class SneakerRack(models.Model):
    subscriber = models.ForeignKey('subscribers.Subscriber', related_name='+', null=False, on_delete=models.CASCADE)
