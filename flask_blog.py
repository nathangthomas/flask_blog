from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '8b623f2c0590d698f3ba4dd622d02724'
# make this an env var at some ponint

posts = [
    {
        'author': 'Nathan Thomas',
        'title': 'Blog Post 1',
        'content': 'Content of my very first post.',
        'date_posted': 'March 18th, 2020'
    },
    {
        'author': 'Camille Terry',
        'title': 'Blog Post 2',
        'content': 'Content of another post.',
        'date_posted': 'March 19th, 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
