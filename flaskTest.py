# We import the markdown library
import markdown
from flask import Flask
from flask import render_template
from flask import Markup

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
	return render_template("index.html")


@app.route('/about')
def about():
        return render_template("about.html")

@app.route('/my-work')
def work():
        return render_template("my-work.html")

@app.route('/contact')
def contact():
        return render_template("contact.html")

#just playing with markdown posts
def markDownDemo():
    content = """
    testDemo
    #i am mrkdown
    """

    content = Markup(markdown.markdown(content))
    return  render_template('')

if __name__ == "__main__":
    app.run()
