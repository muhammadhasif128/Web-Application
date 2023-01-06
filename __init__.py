from flask import Flask, render_template, request, redirect, url_for
from Forms import CreateUserFrom

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/createUser', methods=['GET', 'POST'])
def create_user():
    create_user_form = CreateUserFrom(request.form)
    if request.method == 'POST' and create_user_form.validate():
        return redirect(url_for('home'))
    return render_template('createUser.html', form=create_user_form)


@app.route('/successreg', methods=['POST'])
def successreg():
    return render_template('output.html')


if __name__ == '__main__':
    app.run()