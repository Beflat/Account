# encoding: UTF-8
# Create your views here.
from account.forms import AccountLogForm, AccountLogSearchForm
from account.managers import AccountLogManager
from account.models import AccountLog
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.context import RequestContext
import logging


def index(request):
    
    searchParam = request.GET.dict()
    
    form = AccountLogSearchForm(request.GET)
    searchParam = {}
    if form.is_valid():
        searchParam = form.cleaned_data
    
    
    manager = AccountLogManager()
    search_result = manager.search(**searchParam)
    
    paginator = Paginator(search_result, 5)
    page = request.GET.get('page')
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    
    return render(request, 'account_log/index.html', {'list': list, 'form': form, 'pager': paginator}, context_instance = RequestContext(request))


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


