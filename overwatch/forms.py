from django import forms
from .models import Overwatch
#DataFlair
class OverwatchCreate(forms.ModelForm):
    class Meta:
        model = Overwatch
        fields = '__all__'