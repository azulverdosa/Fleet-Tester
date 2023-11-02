from django.db import models
import random

class Vehicle(models.Model):
    uuid = models.CharField(default=random.randint(0, 2**32 - 1), max_length=16, db_column='uuid')
    identifier = models.CharField(max_length=255, db_column='identifier')

class Report(models.Model):
    uuid = models.CharField(primary_key=True, default=random.randint(0, 2**32 - 1), max_length=16, db_column='uuid')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, db_column='vehicles_uuid')


