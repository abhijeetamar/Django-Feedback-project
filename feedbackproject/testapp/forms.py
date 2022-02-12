from django import forms
from django.core import validators

def starts_with_d(value):
    if value[0] !='d':
        raise forms.ValidationError('name should start with d')

class FeedbackForm(forms.Form):
    name=forms.CharField(validators=[starts_with_d])
    rollno=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea,validators=[validators.max_lengthValidator(40)],validators=[validators.min_lengthValidator(10)])

    def clean_name(self):
        inputname=self.cleaned_data['name']
        if len(inputname)<4:
            raise forms.ValidationError("The length of the name filled should be >=4")
        return inputname

