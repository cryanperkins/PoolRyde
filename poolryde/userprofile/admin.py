from django.contrib import admin
from .models import UserProfile


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {'self_description': ('self_description',), 'line_of_work': ('line_of_work',), 'owns_car': ('owns_car',), 'vehicle_model': ('vehicle_model',), 'hobbies': ('hobbies',)}
    class Meta:
        model = UserProfile

admin.site.register(UserProfile, UserProfileAdmin)