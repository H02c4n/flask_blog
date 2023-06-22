from flask import Flask, render_template
app = Flask(__name__)

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
    return render_template('about.html')






if __name__ == "__main__":
    app.run(debug=True)