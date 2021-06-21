from django import forms
# from django.contrib.auth.models import User
from .models import Hobby
# from django.contrib.auth.forms import UserCreationForm

class HobbyForm(forms.ModelForm):
    

    class Meta:
        model = Hobby
        fields = ['name','description','hobby_img']
       