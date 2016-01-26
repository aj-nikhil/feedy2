from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.core import validators

# Create your models here.


class Customer(AbstractBaseUser):
    username = models.CharField(_('username'), max_length=100, unique=True,
                                help_text=_('Required. 100 characters or fewer. Letters, digits and '
                                            '@/./+/-/_ only.'),
                                validators=[
        validators.RegexValidator(r'^[\w.@+-]+$',
                                  _('Enter a valid username. '
                                    'This value may contain only letters, numbers '
                                    'and @/./+/-/_ characters.'), 'invalid'),
    ],
        error_messages={
            'unique': _("A user with that username already exists."),
    })
    first_name = models.CharField(_('first name'), max_length=100, blank=True)
    last_name = models.CharField(_('last name'), max_length=100, blank=True)
    email = models.EmailField(_('email address'), blank=True)
