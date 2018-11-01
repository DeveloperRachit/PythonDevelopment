from django.db import models

# Create your models here.
class Airport(models.Model):
    code=models.CharField(max_length=3)
    city=models.CharField(max_length=64)
    def __str__(self):
        return f"{self.city} ({self.code}) "


class Flight(models.Model):
      origin=models.ForeignKey(Airport,on_delete=models.CASCADE, related_name="departures")
      destination=models.CharField(max_length=64)
      duration=models.IntegerField()

      def _str_(self):
        return f"{self.origin} to {self.destination}"
       