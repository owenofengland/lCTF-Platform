#!/bin/bash

python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python3 db_init.py
export FLASK_APP=ctf
flask run
