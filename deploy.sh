#!/bin/bash
git pull
source venv/bin/activate
pip install -U pip
pip install -r requirements.txt
python manage.py migrate
sudo systemctl restart workouts