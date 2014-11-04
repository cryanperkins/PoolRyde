from django.shortcuts import render, render_to_response, RequestContext
from django.contrib import messages
from forms import SignUpForms
from .models import SignUp

# Create your views here.

def home(request):
    context = RequestContext
    form = SignUpForms(request.POST)
    #form = SignUpForms(request.POST or None)
    if request.method == 'GET':
        form = SignUpForms()

    if form.is_valid():
        save_post = form.save()
        messages.success(request, 'You are signed up!')

    return render_to_response("signup.html", locals(),
                              context_instance=RequestContext(request))
