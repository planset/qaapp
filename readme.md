README
======
自分用の暗記カード


機能
=========

* カードを追加、編集、削除できる
* カードを見ることができる

それだけであーる


Install
========
1. MySQL databaseを用意

  dbを作成して server/db.sql を実行する

2. API server側を動かす
  ```bash
  virtualenv --no-site-packages env
  source env/bin/activate
  pip install -r server/requires.txt
  cd server
  cp config.py.sample config.py
  # edit config.py
  python app.py
  ```
3. Client側を動かす
  ```bash
  cd client/www/js
  cp config.js.sample config.js
  # edit config.js
  cd ../
  python -m SimpleHTTPServer [ポート番号(デフォルトは8000)]
  
  # python3 -m http.server [ポート番号(デフォルトは8000)]
  ```

4. ブラウザでアクセス

  http://localhost:8000


LICENSE
=========
Copyright (c) 2015 Daisuke Igarashi
Released under the MIT license
http://opensource.org/licenses/mit-license.php

