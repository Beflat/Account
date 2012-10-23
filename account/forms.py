from account import models
from account.models import AccountLog, Category
from django import forms
from django.forms.models import ModelForm



class AccountLogForm(ModelForm):
    
    class Meta:
        model = AccountLog

class AccountLogSearchForm(forms.Form):
    category     = forms.ModelChoiceField ( Category.objects.filter(), required=False)
    logDate_from = forms.DateField(required=False)
    logDate_to   = forms.DateField(required=False)
    created_from = forms.DateTimeField(required=False)
    created_to   = forms.DateTimeField(required=False)
    price_from   = forms.IntegerField(required=False)
    price_to     = forms.IntegerField(required=False)
    