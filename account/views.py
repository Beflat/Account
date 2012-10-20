# encoding: UTF-8
# Create your views here.
from account.models import AccountLog
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
import logging


def index(request):
    
    list = AccountLog.objects.filter().order_by('logDate')
    
    return render(request, 'account_log/index.html', {'list': list})


def batch(request):
    
    messages.add_message(request, messages.SUCCESS, '処理を実行しました。')
    return redirect('account.views.index')
