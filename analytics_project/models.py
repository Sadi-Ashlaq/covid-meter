from django.db import models

# Create your models here.

class Country(models.Model):
    Country = models.CharField(max_length=100)
    Total_Cases = models.IntegerField()
    New_Cases = models.IntegerField()
    Total_Deaths = models.IntegerField()
    New_Deaths = models.IntegerField()


    def __str__(self):
        return self.Country