#!/bin/bash
script_dir=$(cd $(dirname ${BASH_SOURCE:-$0}); pwd)

cd $script_dir
cd www

if [ ! -e js/config.js ]; then
	cp js/config.js.sample js/config.js
fi

_RES=`python -V 2>&1`
PYTHON_VERSION=${_RES#* }
PYTHON_MAIN_VERSION=${PYTHON_VERSION%%.*}

if [ $PYTHON_MAIN_VERSION -eq 2 ]; then
	python -m SimpleHTTPServer
else
	python3 -m http.server
fi
