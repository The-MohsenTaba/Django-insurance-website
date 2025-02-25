from django import forms
from .models import User, UserInfo, Insurance
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate



class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        exclude = ['username']
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'father_name': 'نام پدر',
            'national_id': 'کد ملی',
            'sex': 'جنسیت',
            'birth_date': 'تاریخ تولد',
            'job_title': 'شغل',
            'marriage': 'وضعیت تاهل',
            'job_address': 'آدرس محل کار',
            'home_address': 'آدرس محل سکونت',
            'postal_code': 'کدپستی',
            'phone_number': 'شماره تماس',

        }
        error_messages = {}
class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = ['payment_method','plan']
        labels = {
            'payment_method':"روش پرداخت"
            ,'plan':'طرح'
        }
        widgets = {
            'payment_method': forms.Select(attrs={'id': 'paymentMethod'}),
            'plan': forms.Select(attrs={'id': 'insurancePlan'}),
        }