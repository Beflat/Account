# Create your views here.
from account.models import AccountLog
from django.http import HttpResponse
from django.shortcuts import render, redirect
import logging


def index(request):
    
    list = AccountLog.objects.filter().order_by('logDate')
    
    return render(request, 'account_log/index.html', {'list': list})


def batch(request):
    
    
    return redirect('account.views.index')
