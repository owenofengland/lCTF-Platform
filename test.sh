#!/bin/bash

source env/bin/activate
export FLASK_APP=ctf
export FLASK_DEBUG=1
flask run
