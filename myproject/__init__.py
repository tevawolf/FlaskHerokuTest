import os
from flask import Flask, redirect, url_for, flash, render_template
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

app = Flask(__name__, static_folder='static', template_folder='templates')

# Often people will also separate these into a separate config.py file
app.config['SECRET_KEY'] = 'mysecretkey'
# basedir = os.path.abspath(os.path.dirname(__file__))

# Heroku Postgresアドオンを追加した場合、環境変数DATABASE_URLに
# PostgreSQLデータベースの接続先URLがセットされるので、この値が
# セットされているとき(Heroku上で動作するとき)はそれを使い、
# セットされていないとき(ローカルでのデバッグなど)はローカルのSQLiteデータベースを使うようにする。

# SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
#
# app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)
# Migrate(app,db)