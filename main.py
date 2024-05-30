from flask import *

app = Flask(__name__)

# @app.route('/')
# def message():
#     return '<h1>This is rendering template</h1>'



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about/<username>')
def message(username):
    return render_template('message.html', name=username)

@app.route('/embed/<int:number>')
def table(number):
    return render_template('embed.html', n=number)


if __name__ == '__main__':
    app.run(debug=True)



