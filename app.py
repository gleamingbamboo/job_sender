from flask import Flask, render_template, flash, redirect
from config import Config
from forms import LoginForm

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
@app.route('/index')
def hello_world():
    user = {'username': 'Edward'}
    return render_template('index.html', title="Keklo!", user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

if __name__ == '__main__':
    app.run()
