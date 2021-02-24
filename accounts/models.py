from django.db import models


# Create your models here.
class User(models.Model):

    email = models.EmailField(primary_key=True)
    is_anonymous = False
    is_authenticated = True
    last_login = models.DateTimeField(auto_now_add=True)
    REQUIRED_FIELDS = ()
    USERNAME_FIELD = 'email'
    