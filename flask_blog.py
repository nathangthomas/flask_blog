from flask import Flask, render_template, url_for
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
