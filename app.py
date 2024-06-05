from flask import * #Import the class

app = Flask(__name__)   #Create the object of the class

@app.route('/')  #Decorator defines the route
def hello():
    return "<h1>Hello, World!</h1>"

# Setting cookies
@app.route('/cookie')
def cookie():   #The / acts like an index page
    res = make_response('<h1>Cookie Is Set</h1>')
    res.set_cookie('east africa', 'kenya')
    return res

@app.route('/cookie1')
def cookie2():   #The / acts like an index page
    res = make_response('<h1>The Second cookie Is Set</h1>')
    res.set_cookie('Ford', 'Raptor')
    return res

# Reading cookies
@app.route('/getcookie')
def read_cookies():   #The / acts like an index page
    Ford = request.cookies.get('Ford')
    return f'The value of the ford cookie is: {Ford}'

# Deleting cookies
@app.route('/deletecookie')
def delete_cookie():   #The / acts like an index page
    res = make_response('<h1>The cookie is deleted</h1>')
    res.set_cookie('Ford', '', expires=0)
    return res



# Multiple options
@app.route('/setcookie')
def set_cookie():
    res = make_response('cookie')
    res.set_cookie('sport', 'football', max_age=60*60*24, secure=True, httponly=True)


####
@app.route('/index')
def index():   
    theme = request.cookies.get('theme', 'light')
    return render_template_string (
        """
        <html>
        <body class="{{ theme }}">
            <h1>Hello, World!</h1>
            <a href="/settheme/dark'>Dark Theme</a>

        """, theme=theme
    )

####
@app.route('/settheme/<theme>')
def set_theme(theme):   #The / acts like an index page
    res = make_response(f'Theme set to {theme}')
    res.set_cookie('theme', theme, max_age=60*60*365)
    return res



# @app.route('/sasa/jina')
# def sasa():   #The / acts like an index page
#     return "Wazgood big man ting"  

# #App routing - map to specific url with associated function
# @app.route('/about')
# def about():   #The / acts like an index page
#     return "<h1>About Us Page</h1>"  

# #Variable rules
# @app.route('/user/<username>')
# def showUser(username):   #The / acts like an index page
#     return f'Good afternoon, I am {username}'  


# #pass int
# @app.route('/user/<int:user_id>')
# def showId(user_id):   #The / acts like an index page
#     return f'Your ID is  {user_id}'  


# #Add URL rule()
# #Add url_rule(<url_rule>, <endpoint>, <view_function>) 
# def profile():
#     return 'This is my profile'
# app.add_url_rule('/profile', "profile",profile)


# #URL Building
# #url for() -- dynamic building
# @app.route('/director')
# def director():k
#     return '<h1>director</h1>'

# @app.route('/instructor')
# def instructor():
#     return '<h1>Instructor</h1>'

# @app.route('/student')
# def student():
#     return '<h1>student</h1>'

# @app.route('/personnel/<name>')
# def personnel(name):
#     if name == 'director':
#         return redirect(url_for('director'))
#     if name == 'instructor':
#         return redirect(url_for('instructor'))
#     if name == 'student':
#         return redirect(url_for('student'))


if __name__ == '__main__':
    app.run(debug=True)   #Specifies port number and host address








