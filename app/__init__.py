from flask import Flask
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_sqlalchemy import SQLAlchemy
from flask_nav.elements import *
from app.views import init_view

#实例化Bootstrap对象
bootstrap=Bootstrap()
#实例化Nav对象
nav=Nav()
#实例化db对象 先不传递参数
db = SQLAlchemy()


#创建app对象的函数
def create_app():
    #1.创建app对象  然后进行配置
    app=Flask(__name__)
    #引入secret_key
    app.config.from_pyfile('config')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3306/flasktest1'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    bootstrap.init_app(app)
    navbar=Navbar('Bootstrap测试',
              View('主页','index'),
              View('项目','services'),
              View('服务','projects'),
              View('关于','about')
              )
    nav.register_element('top',navbar)
    nav.init_app(app)
    db.init_app(app)
    init_view(app)
    return app