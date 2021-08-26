from django.db.models.fields import DateField, EmailField
from django import forms
from .models import ecodatabase #ecodatabase is a class name in model.py which is imported here

class ProfileForm(forms.ModelForm):    
    class Meta:
        model = ecodatabase #model class name
        fields = "__all__" # all filds will be filled up

        widgets = {
            "name" : forms.TextInput(attrs={"placeholder": "Name*", "class": "form-control input-lg", "type" : "text", "id":"name", "name":"name"}),
            "email" : forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control input-lg", "type" : "email", "id":"email", "name":"email"}),
            "phone" : forms.TextInput(attrs={"placeholder": "Phone", "class": "form-control input-lg", "type" : "text", "id":"phone", "name":"phone"}),
            "message" : forms.Textarea(attrs={"placeholder": "Message", "class": "form-control input-lg","id":"comments", "name":"comments"})
        }


