
from app.forms import LoginForm
from flask import render_template,flash



def init_view(app):
    @app.route("/")
    def index():
        return render_template('index.html', title='首页')

    @app.template_test("current_link")
    def is_current_link(link):
        return link == request.path

    @app.route("/services")
    def services():
        return 'Services'

    @app.route("/about")
    def about():
        return 'About'

    @app.route("/projects")
    def projects():
        return 'Projects'

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()  # 创建登陆表单对象
        flash('登陆成功')
        return render_template('login.html',
                               title="登陆",
                               form=form)
