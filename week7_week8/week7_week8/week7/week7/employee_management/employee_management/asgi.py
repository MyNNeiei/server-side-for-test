"""
ASGI config for employee_management project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_management.settings')

application = get_asgi_application()

import os
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    os.path.join(SETTINGS_PATH, 'templates'),
)