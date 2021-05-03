from .import db


#角色表
class Role(db.Model):
    # 表名
    __tablename__ = 'roles'
    # 表中的结构
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=True)
    users = db.relationship('User', backref = 'role')

# 用户表
class User(db.Model):
    # 表名
    __tablename__ = 'users'
    # 表中的结构
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(40), nullable=True)
    email=db.Column(db.String(20),nullable=True)
    age=db.Column(db.Integer,nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @staticmethod
    def on_created(target,value,oldvalue,initiator):
        print('target:%s'%target)
        print('on_created:%s'%value)
        target.role=Role.query.filter_by(name='user').first()
        db.session.add(target)
        db.session.commit()


#属性监听。listen()的参数
db.event.listen(User.name,'set',User.on_created)


