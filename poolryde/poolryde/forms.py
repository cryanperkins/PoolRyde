__author__ = 'Ryan Perkins'
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Submit
from userprofile.models import UserProfile



class MyRegistrationForm(UserCreationForm):

    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1')

    def __init__(self, *args, **kwargs):
        super(MyRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Create your screen name'
        self.fields['email'].label = 'Email'
        self.fields['password1'].label = 'Create a password'
        self.fields['password2'].label = 'Confirm your password'


    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])
        profile = UserProfile(user=user)

        profile.user = user
        profile.user.self_description = "self_description"
        profile.user.line_of_work = "line_of_work"
        profile.user.hobbies = "hobbies"
        profile.user.owns_car = "owns_car"
        profile.user.vehicle_model = "vehicle_model"

        if commit:
            user.save()
            profile.save()

        return user
