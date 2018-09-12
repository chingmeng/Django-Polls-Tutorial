from django import forms
from .models import Choice, Question, mModel

class mModelForm(forms.ModelForm):

    class Meta:
        model = mModel
        fields = ('name', 'gender', 'age', 'email', 'dob', 'job')

