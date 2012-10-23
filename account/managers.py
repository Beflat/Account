from account.models import AccountLog
from django.db import models
import datetime
import time



class AccountLogManager(models.Manager):
    
    def search(self, order='-logDate', **kwargs):
        conditions = {}
        
        if kwargs.get('logDate_from', None) != None:
            conditions['logDate__gte'] =  kwargs['logDate_from']
        if kwargs.get('logDate_to', None) != None:
            conditions['logDate__lte'] = kwargs['logDate_to']
        if kwargs.get('category', None) != None:
            conditions['category'] = kwargs['category']
        if kwargs.get('created_from', None) != None:
            conditions['created__gte'] = kwargs['created_from']
        if kwargs.get('created_to', None) != None:
            conditions['created__lte'] = kwargs['created_to']
        if kwargs.get('price_from', None) != None:
            conditions['price__gte'] = kwargs['price_from']
        if kwargs.get('price_to', None) != None:
            conditions['price__lte'] = kwargs['price_to']
        
        return AccountLog.objects.filter(**conditions).order_by(order)
        