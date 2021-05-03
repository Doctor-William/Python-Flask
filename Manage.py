from flask import Flask,url_for
from flask_script import Manager
from app import *
from flask_migrate import Migrate,MigrateCommand
from app.models import User,Role

app = create_app()
#创建Manager对象
manager=Manager(app)
migrate=Migrate(app,db)
manager.add_command('db',MigrateCommand)







if __name__=='__main__':
    #app.run(host='0.0.0.0',port=5000)
    manager.run()
