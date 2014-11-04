from django.contrib import admin
from .models import SignUp
# Register your models here.

class SignUpAdmin(admin.ModelAdmin):
    prepopulated_fields = {'last_name': ('last_name',)}
    class Meta:
        model = SignUp

admin.site.register(SignUp, SignUpAdmin)
