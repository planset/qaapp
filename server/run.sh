#!/bin/bash
script_dir=$(cd $(dirname ${BASH_SOURCE:-$0}); pwd)

cd $script_dir
source ../env/bin/activate
python app.py runserver --host=0.0.0.0 --port=9092 --reload
