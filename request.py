from flask import *

app = Flask(__name__)

@app.route('/')
def client():
    return render_template('clients.html')

@app.route('/success', methods=['POST', 'GET'])
def showData():
    if request.method == 'POST':
        result = request.form
        return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)