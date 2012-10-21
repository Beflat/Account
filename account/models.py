from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name
    


class AccountLog(models.Model):
    category = models.ForeignKey(Category)
    price = models.IntegerField()
    memo = models.CharField(max_length=255, blank=True)
    logDate = models.DateField()
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    
    def __unicode__(self):
        return self.logDate

