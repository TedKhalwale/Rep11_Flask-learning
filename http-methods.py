from flask import *

app = Flask(__name__)

# @app.route('/login', methods = ['POST'])
# def login():
#     uname=request.form['uname']
#     password=request.form['pass']
#     if uname == 'gen' and password == 'trial':
#         return "Hello there %s"%uname  #{uname}

# @app.route('/login', methods = ['GET'])
# def login():
#     uname=request.args.get('uname')
#     password=request.args.get('pass')

#     if uname == 'gen' and password == 'trial':
#         return "Hello there %s"%uname  #{uname}


# if __name__ == '__main__':
#     app.run(debug=True)