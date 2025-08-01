from django.db import models

class Transaction(models.Model):
    amount = models.FloatField()
    category = models.CharField(max_length=100)
    date = models.DateField()
