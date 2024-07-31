from flask import Flask, render_template, request, redirect, url_for
import markdown

app = Flask(__name__)

@app.before_request
def before_request():
    if 'X-Forwarded-Proto' in request.headers:
        if request.headers['X-Forwarded-Proto'] == 'http' and not app.debug:
            url = request.url.replace('http://', 'https://', 1)
            return redirect(url, code=301)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/templates/index.html')
def index2():
    return render_template('index.html')

@app.route('/templates/docs.html')
def docs():
    return render_template('docs.html')

@app.route('/iosplan')
def display_markdown():
    with open('static/iosplan.md', 'r') as f:
        content = f.read()
    
    return render_template('iosplan.html', content=content)

@app.route('/webplan')
def display_markdown_web():
    with open('static/webplan.md', 'r') as f:
        content = f.read()

    return render_template('webplan.html', content=content)

if __name__ == '__main__':
    app.run(debug=True)
