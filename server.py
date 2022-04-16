from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)



# ROUTES



@app.route('/homepage')
def hello_name():
    return render_template('homepage.html')


@app.route('/sound/<name>')
def people(name='Letter_B'):
    return render_template('sound.html')





if __name__ == '__main__':
   app.run(debug = True)