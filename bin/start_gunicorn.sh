#!/bin/bash

source /root/code/vladbalandin/
exec gunicorn -c "/root/code/vladbalandin/config/gunicorn_config.py" config.wsgi


