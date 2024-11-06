from django import forms
from .models import Client, ServiceProvider, ServiceHistory

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_id','name','username','password','email','city','pincode','landmark' ,'mobile']  # Adjust fields as necessary

class ServiceProviderForm(forms.ModelForm):
    class Meta:
        model = ServiceProvider
        fields = ['sp_id','name', 'adhar_card','city','pincode', 'mobile','username','password','skills']  # Adjust fields as necessary

class ServiceHistoryForm(forms.ModelForm):
    class Meta:
        model = ServiceHistory
        fields = ['client', 'sp_id', 'service', 'date','amount','rating','pending_completion']