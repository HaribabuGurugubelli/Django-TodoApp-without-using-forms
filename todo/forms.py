from django.forms import ModelForm
from .models import *


class updateForm(ModelForm):
    class Meta:
        model = todo
        fields = '__all__'
