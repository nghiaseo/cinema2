from django.db import models


# Create your models here.
class Cinema(models.Model):
    name = models.CharField(max_length=100)
    number_of_seats = models.IntegerField()
    number_of_seats_per_row = models.IntegerField()


class Seat(models.Model):
    number = models.IntegerField()
    booked = models.BooleanField(default=False)
