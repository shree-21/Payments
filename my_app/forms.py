from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.formfields import PhoneNumberField

from django.utils.translation import gettext as _

from django.forms.fields import DateField
from django.forms.widgets import SelectDateWidget



class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class SignupForm(forms.Form):

    USER_CHOICES = [
        ('LANDLORD', 'Landlord'),
        ('TENANT', 'Tenant')
    ]

    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    middle_name = forms.CharField(max_length=30, required=False)
    
    YEARS= [x for x in range(1940,2021)]
    birth_date = forms.DateField(widget=SelectDateWidget(years=YEARS))

    phone_number = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': _('Phone')}), 

                       label=_("Phone number"), required=False)

    user_choice = forms.ChoiceField(choices=USER_CHOICES, widget=forms.RadioSelect())

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.middle_name = self.cleaned_data['middle_name']
        user.birth_date = self.cleaned_data['birth_date']
        user.phone_number = self.cleaned_data['phone_number']
        user.user_choice = self.cleaned_data['user_choice']
        user.save()


class SelectValue(forms.Form):
    tenant_email = forms.EmailField()