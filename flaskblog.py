from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'UmB1Dj17GxyGmV3e8f7RU92oP0rr45nG'

posts = [
    {
        'author': 'Evan Lane',
        'title': 'First Post',
        'content': 'This is my first blog post, pretty cool!',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Evan Lane',
        'title': 'Second Post',
        'content': 'This is my second blog post, I think I am starting to get the hang of this now!',
        'date_posted': 'April 21, 2018'
    },
    {
        'author': 'Cookie Monster',
        'title': 'Cookies Are Great',
        'content': 'I see a lot of talk about diets these days. But what about an all cookie diet?',
        'date_posted': 'April 22, 2018'
    },
]

# @ is a decorator
@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    # return render_template('about.html', title='About')
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
