from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date

# Create your models here.
class CustomUser(AbstractUser):

    USER_CHOICES = [
        ('LANDLORD', 'Landlord'),
        ('TENANT', 'Tenant')
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(blank=True, null=True, default=date.today)
    phone_number = PhoneNumberField(blank=True)
    user_choice = models.CharField(max_length=10, choices=USER_CHOICES, default='Tenant')

    def __str__(self):
        return self.email