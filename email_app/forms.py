from django import forms
from email_app.models import Student
class studentforms(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'