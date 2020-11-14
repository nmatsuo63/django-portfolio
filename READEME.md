# Git 手順

- GitHub でリポジトリを作る
  - .gitignore のみ作る場合が多い
- ローカルで git clone https://github.com/nmatsuo63/xxxx.git
- ファイル編集
- git add .
- git commit -m "some commments"
- git push origin master

# 仮想環境有効化

2184 python3 -m venv myenv
2185 source myenv/bin/activate

# requirements.txt 作成

2186 touch requirements.txt
2189 pip3 install -r requirements.txt

# プロジェクト作成＆サーバー起動

2190 django-admin startproject mysite .
2191 python3 manage.py migrate
2192 python3 manage.py runserver
