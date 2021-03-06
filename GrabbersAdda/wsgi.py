"""
WSGI config for GrabbersAdda project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""
path = "/home/ajaypatel/Django/affiliate-project/GrabbersAdda"

import os
import django

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GrabbersAdda.settings')

django.setup()

application = get_wsgi_application()
