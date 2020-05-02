
#from __future__ import unicode_literals
#from django.utils.translation import ugettext_lazy as _

#from djangoprofiles.signals import create_user_profile, save_user_profile
#from django 
from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    def ready(self):
        import users.signals
        
