from django import forms
from .models import Website,Username,TaoPian
class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = ['text']
        labels = {'text': ''}
class UsernameForm(forms.ModelForm):
    class Meta:
        model = Username
        fields = ['text','text2']
        labels = {'text': '','text2':''}
        widgets = {'text':'','text2':''}
class TaoPianForm(forms.ModelForm):
    class Meta:
        model=TaoPian
        verbose_name = 'TaoPianFangZhu'  
        verbose_name_plural = 'TaoPianFangZhu'  
        fields=['text','text2']
        labels={'text':'','text2':''}