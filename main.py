import os,sys

import django.core.handlers.wsgi
import django.core.signals
import django.db
import django.dispatch.dispatcher

# Google App Engine imports.
from google.appengine.ext.webapp import util

# Force Django to reload its settings.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rev_eng2.settings")
from django.conf import settings
settings._target = None

# Unregister the rollback event handler.
django.dispatch.dispatcher.disconnect(
  django.db._rollback_on_exception,
  django.core.signals.got_request_exception)


def main():
    # Create a Django application for WSGI.
    application = django.core.handlers.wsgi.WSGIHandler()

    # Run the WSGI CGI handler with that application.
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()
