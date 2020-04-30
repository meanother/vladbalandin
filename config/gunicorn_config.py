import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

command = os.path.join(BASE_DIR, 'env/bin/gunicorn')
pythonpath = os.path.join(BASE_DIR, 'config')
#bind = '0.0.0.0:8001'
bind = '0.0.0.0:9000'
workers = 3
user = 'root'
limit_request_field = 3200
limit_request_field_size = 0
#errorlog = os.path.join(BASE_DIR, 'backend.log')
#loglevel = 'info'
#accesslog = os.path.join(BASE_DIR, 'backend.log')
access_log_format = '%(t)s %(h)s %(r)s %(q)s %(s)s %(T)s %(p)s'
raw_env = 'DJANGO_SETTINGS_MODULE=config.settings'
redirect_stderr = True
autorestart = True
