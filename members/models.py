# member models

import random
from django.db import models
from django.contrib.auth.models import User
from django.utils.hashcompat import sha_constructor


from alkawsarsite.languages import *
from alkawsarsite.issues.models import Issue


class UserProfile(models.Model):
    
    user = models.OneToOneField(User)
    resetpassword_key = models.CharField(null=True, max_length=40)
    
    def set_resetpassword_key(self):
        if not self.user:
            raise Exception('User not set')
        salt = sha_constructor(str(random.random())).hexdigest()[:5]
        self.resetpassword_key = sha_constructor(salt+self.user.username).hexdigest()


        
