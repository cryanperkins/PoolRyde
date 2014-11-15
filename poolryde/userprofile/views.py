from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.views.generic import ListView
from .models import UserProfile
from forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile



# Create your views here.
#@login_required
def user_profile(request):
    user = request.user
    profile = user.profile
    # todo create a dictionary to pass in the logged in userprofile attributes
    # d = {}
    # d.update({"line_of_work": profile.line_of_work})
    # d.update({"hobbies: profile.hobbies})
    # return render_to_response("profile.html", d)
    # template tags match {{ line_of_work }}, {{ hobbies }}
    context = {"profile_description": profile.self_description}



    return render_to_response('profile.html', context)



def profile_success(request):
    return render_to_response('profile_success.html')

#class Index(ListView):
   # queryset = UserProfile.objects.all()
   # template = "profile.html"
