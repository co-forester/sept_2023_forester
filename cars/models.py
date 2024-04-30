from django.db import models

class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
    brand = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    engine = models.IntegerField()
    year = models.IntegerField()
