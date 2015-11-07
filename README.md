README
======
暗記用のメモカード


FEATURES
=========

* カードを追加、編集、削除できる
* カードを見ることができる

それだけであーる


Install
========
1. Download and settings

  ```bash
  git clone https://github.com/planset/qaapp.git

  cd qaapp

  virtualenv --no-site-packages env
  pip install -r server/requires.txt
  ```

2. Run API server
  ```bash
  server/run.sh
  ```

3. Run client
  ```bash
  client/run.sh
  ```

4. ブラウザでアクセス

  http://localhost:8000


LIBRARIES
=========
* [Flask](http://flask.pocoo.org)
* [Flask-Script](https://flask-script.readthedocs.org)
* [Flask-Migrate](https://flask-migrate.readthedocs.org)

* [SQLAlchemy](http://www.sqlalchemy.org)
* [alembic](https://alembic.readthedocs.org)


LICENSE
=========
Copyright (c) 2015 Daisuke Igarashi
Released under the MIT license
http://opensource.org/licenses/mit-license.php

