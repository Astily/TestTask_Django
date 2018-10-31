import datetime

from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import SelectDateWidget

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        exclude = ['password', 'last_login', 'is_superuser', 'groups', 'user_permissions', 'date_joined',
                   'email', 'is_active', 'is_staff', 'username']
        widgets = {
            'birth': SelectDateWidget(years=range(1950, datetime.datetime.now().year)),
        }

