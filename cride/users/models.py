"""User model"""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utilities
from cride.utils.models import CRideModel


class User(CRideModel, AbstractUser):
    """User model,
    
    Extend from Django's abstract User, change the username field 
    to email and add some extra fields.
    """
    email = models.EmailField(
        'email_address',
        unique=True,
        error_message={
            'unique': 'A user with that email already exist.'
        }
    )
    phone_number = models.CharField(
        max_lenght=17,
        blank=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    is_client = models.BooleanField(
        'client',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries.'
            'Clients are the main type of user. '
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=False,
        help_text='Set to true when the user have verified its email address'
    )