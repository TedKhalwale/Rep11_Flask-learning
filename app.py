from flask import Flask, url_for, redirect #Import the class

app = Flask(__name__)   #Create the object of the class

@app.route('/')  #Decorator defines the route
def hello():
    return "<h1>Hello, World!</h1>"

@app.route('/sasa')
def salamu():   #The / acts like an index page
    return "Wazgood man" 

@app.route('/sasa/jina')
def sasa():   #The / acts like an index page
    return "Wazgood big man ting"  

#App routing - map to specific url with associated function
@app.route('/about')
def about():   #The / acts like an index page
    return "<h1>About Us Page</h1>"  

#Variable rules
@app.route('/user/<username>')
def showUser(username):   #The / acts like an index page
    return f'Good afternoon, I am {username}'  


#pass int
@app.route('/user/<int:user_id>')
def showId(user_id):   #The / acts like an index page
    return f'Your ID is  {user_id}'  


#Add URL rule()
#Add url_rule(<url_rule>, <endpoint>, <view_function>) 
def profile():
    return 'This is my profile'
app.add_url_rule('/profile', "profile",profile)


#URL Building
#url for() -- dynamic building
@app.route('/director')
def director():
    return '<h1>director</h1>'

@app.route('/instructor')
def instructor():
    return '<h1>Instructor</h1>'

@app.route('/student')
def student():
    return '<h1>student</h1>'

@app.route('/personnel/<name>')
def personnel(name):
    if name == 'director':
        return redirect(url_for('director'))
    if name == 'instructor':
        return redirect(url_for('instructor'))
    if name == 'student':
        return redirect(url_for('student'))


if __name__ == '__main__':
    app.run(debug=True)   #Specifies port number and host address
