import os
import sys


def fix_imports():
  here = os.path.dirname(__file__)
  dirs = [
      os.path.normpath(os.path.join(here, '..', '..')),
      os.path.normpath(os.path.join(here, 'babel')),
      os.path.normpath(os.path.join(here, 'dulwich')),
      os.path.normpath(os.path.join(here, 'google-apputils-python')),
      os.path.normpath(os.path.join(here, 'google-protorpc', 'python')),
      os.path.normpath(os.path.join(here, 'httplib2', 'python2')),
      os.path.normpath(os.path.join(here, 'jinja2')),
      os.path.normpath(os.path.join(here, 'markupsafe')),
      os.path.normpath(os.path.join(here, 'pytz')),
      os.path.normpath(os.path.join(here, 'pyyaml', 'lib')),
      os.path.normpath(os.path.join(here, 'requests')),
      os.path.normpath(os.path.join(here, 'webapp-improved')),
      os.path.normpath(os.path.join(here, 'werkzeug')),
      os.path.normpath(os.path.join(here, 'webob')),
  ]
  sys.path.extend(dirs)