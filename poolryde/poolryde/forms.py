__author__ = 'Ryan Perkins'
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Submit




class MyRegistrationForm(UserCreationForm):

    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)


    class Meta:
        model = User
        fields = ('username', 'email', 'password1')

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()

        return user
