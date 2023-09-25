from django import forms
from apps.todo.models import Settings

class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ["title",'description','completed']
