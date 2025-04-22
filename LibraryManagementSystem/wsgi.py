import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryManagementSystem.settings')

# Get the WSGI application
application = get_wsgi_application()

# Vercel looks for 'app' as the entry point
app = application
