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

# ブランチ作成からマージまで

2194 git branch
2195 git checkout -b startproject
2196 git branch
2199 git diff
2197 git add .
2198 git status
2200 git commit -m "startproject"
2201 git push origin startproject
2205 git checkout main
2206 git merge startproject
2207 git push origin main

# データ登録

settings.py, models.py, admin.py に行追加
2212 python3 manage.py startapp app
2216 python3 manage.py makemigrations
2217 python3 manage.py migrate
2218 phthon3 manage.py createsuperuser
2220 python3 manage.py runserver
2221 git checkout registerdata
2222 git checkout -b registerdata
2223 git diff
2224 git add .
2225 git commit -m "registerdata"
2226 git push origin registerdata
2227 git checkout main
2228 git merge registerdata
2229 git push origin main
