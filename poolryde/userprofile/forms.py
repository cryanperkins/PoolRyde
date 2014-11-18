__author__ = 'C. Ryan Perkins'

from django import forms
from models import UserProfile


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('self_description', 'line_of_work', 'owns_car', 'vehicle_model', 'hobbies')