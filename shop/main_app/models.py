from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.templatetags.static import static
# Create your models here.

class Profile(models.Model):
    
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    avatar = models.CharField(max_length=500, blank=True)
    birthday = models.DateField(null=True, blank=True)
    bio = models.CharField(max_length=32, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
