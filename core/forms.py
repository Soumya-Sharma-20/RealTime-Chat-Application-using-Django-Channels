from http.client import ImproperConnectionState
from pyexpat import model
from attr import field
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']