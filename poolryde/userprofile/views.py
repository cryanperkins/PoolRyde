from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
#from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.
@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login_success')
    else:
        user = request.user
        profile = user.profile
        form = UserProfileForm(instance=profile)

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('profile.html', args)

    #userid = request.user.id
    #user = User.objects.get(pk=userid)
    #profile = UserProfile.objects.get(user=user.id)
    #account_details = user
#   to do create a dictionary to pass in the logged in userprofile attributes
    #d = {}
    #d.update({"line_of_work": profile.line_of_work})
    #d.update({"hobbies": profile.hobbies})
    #d.update({"self_description": profile.self_description})
    #d.update({"owns_car": profile.owns_car})
    #d.update({"vehicle_model": profile.vehicle_model})
    #d.update({"username": account_details.username})
    #return render_to_response('profile.html', d)
    #template tags match {{ line_of_work }}, {{ hobbies }}, {{profile_description}},


def profile_success(request):
    return render_to_response('profile_success.html')


def edit_profile(request):

    return render_to_response('edit_profile.html')

#class Index(ListView):
   # queryset = UserProfile.objects.all()
   # template = "profile.html"
