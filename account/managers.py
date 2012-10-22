from account.models import AccountLog
from django.db import models
import datetime
import time



class AccountLogManager(models.Manager):
    
    def search(self, **kwargs):
        conditions = {}
        
        if kwargs.has_key('logDate_from'):
            conditions['logDate__gte'] =  kwargs['logDate_from']
        if kwargs.has_key('logDate_to'):
            conditions['logDate__lte'] = kwargs['logDate_to']
        if kwargs.has_key('category'):
            conditions['category'] = kwargs['category']
        if kwargs.has_key('created_from'):
            conditions['created__gte'] = kwargs['created_from']
        if kwargs.has_key('created_to'):
            conditions['created__lte'] = kwargs['created_to']
        
        return AccountLog.objects.filter(**conditions)
        