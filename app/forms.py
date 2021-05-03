from flask_wtf.form import FlaskForm
from wtforms.fields.core import StringField
from wtforms.fields.simple import PasswordField,SubmitField
from wtforms.validators import DataRequired


#定义表单类
class LoginForm(FlaskForm):
    #定义表单中的各个项
    username=StringField(label='用户名',validators=[DataRequired()])#文本框 要求必须输入内容
    #求必须输入内容
    password=PasswordField(label='密码',validators=[DataRequired()])#密码框要求必须输入内容
    #要求必须输入内容
    submit=SubmitField()    #提交按钮