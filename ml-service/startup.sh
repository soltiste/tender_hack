#!/bin/bash
export PYTHONUNBUFFERED=1

uwsgi --http 0.0.0.0:5000 --wsgi-file main.py --callable app --processes 3