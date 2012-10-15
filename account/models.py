from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class AccountLog(models.Model):
    category = models.ForeignKey(Category)
    price = models.IntegerField()
    memo = models.CharField(max_length=255)
    logDate = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

