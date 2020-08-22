from django.db import models
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from home.models import *


@receiver(user_signed_up)
def after_user_signed_up(request, user, **kwargs):
