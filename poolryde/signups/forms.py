from django import forms
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Submit
from models import SignUp

#from .models import SignUp

#class SignUpForm(forms.ModeForm):
 #   class Meta:
 #       model = SignUp

class SignUpForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForms, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-4 blue'
        self.helper.layout = Layout('first_name', 'last_name', 'email', 'phone',)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    first_name = forms.CharField(
        label='First Name:',
        max_length=80,
        required=True,
    )

    last_name = forms.CharField(
        label='Last Name:',
        max_length=80,
        required=True,
    )

    email = forms.EmailField(
        label='Email:',
        max_length=80,
        required=True,
    )

    phone = forms.CharField(
        label='Phone:',
        max_length=20,
        required=False,
    )

    class Meta:
        model = SignUp
