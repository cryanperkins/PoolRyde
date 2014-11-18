from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
#from django.views.generic import ListView
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
@login_required
def user_profile(request):
    userid = request.user.id
    profile = UserProfile.objects.get(id=userid)
    account_details = User.objects.get()
# to do create a dictionary to pass in the logged in userprofile attributes
    d = {}
    d.update({"line_of_work": profile.line_of_work})
    d.update({"hobbies": profile.hobbies})
    d.update({"self_description": profile.self_description})
    d.update({"owns_car": profile.owns_car})
    d.update({"vehicle_model": profile.vehicle_model})
    print d
    return render_to_response('profile.html', d)
    #template tags match {{ line_of_work }}, {{ hobbies }}, {{profile_description}},


def profile_success(request):
    return render_to_response('profile_success.html')


def edit_profile(request):

    return render_to_response('edit_profile.html')

#class Index(ListView):
   # queryset = UserProfile.objects.all()
   # template = "profile.html"
