"""
WSGI config for firstapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

""""
import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise


application = get_wsgi_application()
application = DjangoWhiteNoise(application)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "firstapp.settings")

"""
import os
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "firstapp.settings")
application = Cling(get_wsgi_application())
