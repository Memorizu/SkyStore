from typing import Any
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from users.models import User
from version.forms import StyleForm



class UserRegisterForm(StyleForm, UserCreationForm):
    
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
    
        
class UserProfileForm(StyleForm, UserChangeForm):
    
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar')
        
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        
        self.fields['password'].widget = forms.HiddenInput()
        