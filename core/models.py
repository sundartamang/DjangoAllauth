from django.db import models
from allauth.account.signals import user_logged_in
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

def user_loged_in_received(request,user,**kwargs):
    print(user)
    
user_logged_in.connect(user_loged_in_received,sender=User)