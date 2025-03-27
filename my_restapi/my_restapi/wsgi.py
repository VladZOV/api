"""
WSGI config for my_restapi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from pathlib import Path

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / 'dbenv.env')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_restapi.settings')

application = get_wsgi_application()
