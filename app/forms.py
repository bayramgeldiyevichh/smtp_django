from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["name", "message" "email"]


        widgets = {
            "name":forms.TextInput(attrs={'class':"sm-form-control require", 'placeholder':"Name"}),
            "email":forms.TextInput(attrs={'class':"sm-form-control require", 'placeholder':"example@gmail.com"}),
        }