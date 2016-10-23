# We import the markdown library
import markdown
from flask import Flask
from flask import render_template
from flask import Markup

#wTODO: why dependecie fail?
#from flask_flatpages import FlatPages, pygments_style_defs

app = Flask(__name__)
#flatpages = FlatPages(app) # set to get those extra files

@app.route('/')
@app.route('/index')
@app.route('/home')

#TODO: got kinda bored follow this -> http://www.jamesharding.ca/posts/simple-static-markdown-blog-in-flask/

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
@app.route('/mark')
def markDownDemo():
    content = """
    testDemo
    #i am mrkdown
    """

    #path =  '{}/{}'.format('/content', "longlive.md")

    #flatpages.get_or_404(path)

    content = Markup(markdown.markdown(content))

    return  render_template('markdown.html', content = content)

if __name__ == "__main__":
    app.run()
