from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):

    user = models.OneToOneField(User, primary_key=True)
    self_description = models.TextField(blank=True)
    line_of_work = models.CharField(max_length=50, blank=True)
    hobbies = models.TextField(blank=True)
    owns_car = models.NullBooleanField()
    vehicle_model = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return "account for {0}".format(self.user.username)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])