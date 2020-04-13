from django.db import models


# Create your models here.


class Sneaker(models.Model):
    brand = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=2)
    style = models.CharField(max_length=50)
    subscriber = models.ForeignKey("subscribers.Subscriber", related_name='subscriber', null=True,
                              on_delete=models.SET_NULL)

    def __str__(self):
        return "{} {}".format(self.brand, self.style)


class SneakerRack(models.Model):
    subscriber = models.ForeignKey('subscribers.Subscriber', related_name='+', null=False, on_delete=models.CASCADE)

    def sneakers(self):
        return Sneaker.objects.filter(owner_id=self.subscriber.id)
