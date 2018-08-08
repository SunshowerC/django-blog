"""
WSGI config for my_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

"""
run django app with uWSGI : 
uwsgi --socket mysite.sock --module my_blog.wsgi --chmod-socket=664
or 
uwsgi --ini mysite_uwsgi.ini  
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_blog.settings")

application = get_wsgi_application()
