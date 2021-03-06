import os
import site

try:
    import newrelic.agent
except ImportError:
    newrelic = False


if newrelic:
    newrelic_ini = os.getenv('NEWRELIC_PYTHON_INI_FILE', False)
    if newrelic_ini:
        newrelic.agent.initialize(newrelic_ini)
    else:
        newrelic = False


os.environ.setdefault('CELERY_LOADER', 'django')
# NOTE: you can also set DJANGO_SETTINGS_MODULE in your environment to override
# the default value in manage.py

# Add the app dir to the python path so we can import manage.
wsgidir = os.path.dirname(__file__)
site.addsitedir(os.path.abspath(os.path.join(wsgidir, '../')))

# Explicitly set these so that fjord.manage_utils does the right
# thing.
os.environ['USING_VENDOR'] = '1'
os.environ['SKIP_CHECK'] = '1'

# manage adds vendor to the Python path and otherwise sets up the
# environment.
import manage

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

if newrelic:
    application = newrelic.agent.wsgi_application()(application)

# vim: ft=python
