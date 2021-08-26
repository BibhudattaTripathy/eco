from django.db import models
from django.db.models.fields import CharField, DateField, EmailField, TextField

from django.urls import reverse

# Create your models here.
class ecodatabase(models.Model):
    name =CharField(max_length=30, null= True)
    email =EmailField(null=True)
    phone =CharField(max_length=12, null= True)
    message =TextField(max_length=300, null= True)

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})