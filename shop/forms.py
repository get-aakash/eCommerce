from django import forms
from django.core.exceptions import ValidationError


class StudentForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=40)

    email = forms.EmailField()
    agree = forms.BooleanField(label="I Agree", label_suffix="")
    roll = forms.IntegerField(min_value=0)
    number = forms.DecimalField(min_value=0, max_value=40, decimal_places=1)

    def clean(self):
        value = super().clean()
        name = value["name"]
        email = value["email"]
        if len(name) < 4:
            raise ValidationError("the name should be more than 4")
        if len(email) < 10:
            raise ValidationError("the length of email should be more than 10")
