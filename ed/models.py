from django.db import models


# Create your models here.

class Contractor(models.Model):
    Name = models.CharField(max_length=200)

    def __str__(self):
        return self.Name

class Contract(models.Model):
    Name = models.CharField(max_length=200)

    def __str__(self):
        return self.Name

class Item(models.Model):
    Name = models.CharField(max_length=200)

    def __str__(self):
        return self.Name

class Disclosure(models.Model):
    contractor = models.ForeignKey(Contractor)
    contract = models.ForeignKey(Contract)
    item = models.ForeignKey(Item)
    sum = models.IntegerField()

