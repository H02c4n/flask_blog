from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterForm, LoginForm
app = Flask(__name__)


app.config['SECRET_KEY'] = '51206c77d50dd0e1363c493ba8483ca4'

posts = [
    {
        'author':'Halil',
        'title':'Blog post 1',
        'content': 'First post content',
        'date_posted':'June 21, 2023'
    },
    {
        'author':'Cemal',
        'title':'Blog post 2',
        'content': 'Second post content',
        'date_posted':'June 22, 2023'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="About")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form  = RegisterForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@flask.com' and form.password.data == 'admin':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)



if __name__ == "__main__":
    app.run(debug=True)