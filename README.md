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

# アプリケーション作成

mysite/urls.py, app/urls.py, views.py を作成
settings.py, models.py, admin.py に行追加
2212 python3 manage.py startapp app
2216 python3 manage.py makemigrations
2217 python3 manage.py migrate
2218 phthon3 manage.py createsuperuser
2220 python3 manage.py runserver

# データ登録

- サーバ起動して管理画面（/admin）に遷移し、profile を追加

# トップページを整える

- テンプレートの作成（app/templates/app/base.html, index.html）
- CSS の作成（app/static/css/style.css）
- ロゴの登録（app/static/img/logo.svg）

# 作品リストの作成

models.py で Work クラスを作成
admin.py で Work をインポート
views.py で work データを表示
index.html に work データを表示
style.css で動きをつける
2255 python3 manage.py makemigrations
2256 python3 manage.py migrate
2259 python3 manage.py runserver
2260 git checkout -b worklist
2261 git add .
2262 git commit -m "worklist created"
2263 git push origin worklist
2264 git checkout main
2265 git merge worklist
2266 git push origin main

# 作品詳細リストの作成

app/urls.py で detail ページへの root を作成
views.py で detail ページを作成
index.html に detail ページへのリンクを貼る
template/app/detail.html を作成
