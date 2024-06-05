from flask import *

app = Flask(__name__)

@app.route('/error')
def error():
    return '<h1>Enter the correct password</h1>'

# Homepage
@app.route('/')
def login():
    return render_template('login.html')

# Directives
@app.route ('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['passwd']

    if password == 'sasa':
        res = make_response(render_template('success.html'))
        res.set_cookie('email', email)
        return res
    else:
        return redirect(url_for('error'))


@app.route('/viewprofile')
def profile():
    email = request.cookies.get('email')
    res = make_response(render_template('profile.html', name=email))
    return res

if __name__ == '__main__':
    app.run(debug=True)