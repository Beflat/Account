# encoding: UTF-8
# Create your views here.
from account.forms import AccountLogForm
from account.models import AccountLog
from django.contrib import messages
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
import logging


def index(request):
    
    list = AccountLog.objects.filter().order_by('logDate')
    
    return render(request, 'account_log/index.html', {'list': list})


def batch(request):
    
    messages.add_message(request, messages.SUCCESS, '処理を実行しました。')
    return redirect('account.views.index')


def new(request):
    
    form = AccountLogForm()
    data = {'form': form}
    
    return render(request, 'account_log/new.html', data)


def register(request):
    
    form = AccountLogForm(request.POST)
    
    if form.is_valid:
        form.save()
        messages.add_message(request, messages.SUCCESS, 'データを登録しました。')
        return redirect('account.views.new')
    
    
    data = {'form': form}
    
    messages.add_message(request, messages.ERROR, "結果：" + str(form.errors))
    return render(request, 'account_log/new.html', data)

