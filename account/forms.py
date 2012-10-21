from account.models import AccountLog
from django.forms.models import ModelForm



class AccountLogForm(ModelForm):
    
    class Meta:
        model = AccountLog
    