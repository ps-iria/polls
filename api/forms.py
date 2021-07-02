from django import forms
from api.models import Poll


class ChoiceAddForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = '__all__'
