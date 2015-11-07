#!/bin/bash
script_dir=$(cd $(dirname ${BASH_SOURCE:-$0}); pwd)

cd $script_dir

if [ -e ../env ]; then
	source ../env/bin/activate
fi

if [ ! -e config.py ]; then
	cp config.py.sample config.py
	python app.py db upgrade
fi

python app.py runserver --host=0.0.0.0 --port=9092 --reload
