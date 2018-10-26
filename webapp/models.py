from django.db import models

class stocks(models.Model):
    ticker = models.CharField(max_length=10)
    datee = models.DateField(max_length=100)
    closee = models.IntegerField(max_length=15)


class kosits(models.Model):
    portfolio = models.ForeignKey(stocks, on_delete=models.CASCADE)
    highh = models.IntegerField(max_length=15)
