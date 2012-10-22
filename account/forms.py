from account.models import AccountLog
from django import forms
from django.forms.models import ModelForm



class AccountLogForm(ModelForm):
    
    class Meta:
        model = AccountLog

class AccountLogSearchForm(forms.Form):
    logDate_from = forms.DateField(required=False)
    