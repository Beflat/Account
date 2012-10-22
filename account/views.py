# encoding: UTF-8
# Create your views here.
from account.forms import AccountLogForm, AccountLogSearchForm
from account.managers import AccountLogManager
from account.models import AccountLog
from django.contrib import messages
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
import logging


def index(request):
    
    #list = AccountLog.objects.filter().order_by('logDate')
    searchParam = request.GET.dict()
    manager = AccountLogManager()
    list = manager.search(**searchParam)
    
    form = AccountLogSearchForm(searchParam)
    
    return render(request, 'account_log/index.html', {'list': list, 'form': form})


def batch(request):
    
    type = request.POST.get('action')
    if type == 'd':
        AccountLog.objects.filter(id__in=request.POST.getlist('ids')).delete()
        messages.add_message(request, messages.SUCCESS, '選択したデータを削除しました。')
    else:
        messages.add_message(request, messages.ERROR, '無効なコマンドが選択されました。')
    
    
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


