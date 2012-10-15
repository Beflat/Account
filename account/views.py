# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import logging


def index(request):
    
    logger = logging.getLogger('app')
    logger.info('test message!')
    return render(request, 'account_log/index.html')
