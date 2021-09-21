"""
WSGI config for MyPortfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv
from pathlib import Path

from django.core.wsgi import get_wsgi_application

project_folder = Path(__file__).absolute(
).parent.parent.parent  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyPortfolio.settings')

application = get_wsgi_application()
