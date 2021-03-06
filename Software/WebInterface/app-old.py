# from flask import Flask, render_template, request
# import requests

# app = Flask(__name__)

# @app.route('/', methods=["GET", "POST"])
# def index():
#     url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=c188614b93e3f2335199f223926b87e9'
#     city = 'Las Vegas'

#     if request.method == 'POST':
#         city = request.form.get('city')
        
#     r = requests.get(url.format(city)).json()
#     print(r)


#     weather = {
#         'city' : city,
#         'temperature' : r['main']['temp'],
#         'description' : r['weather'][0]['description'],
#         'icon' : r['weather'][0]['icon'],
#     }

#     # return render_template('weather.html', weather=weather)
#     return render_template('weather.html')


# @app.route('/hello')
# def hello():
#     return 'Hello, World'


# if __name__ == '__main__':
#     app.run()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import *
import os
from werkzeug import secure_filename
app = Flask(__name__)

#searchword = request.args.get('q', '')

UPLOAD_FOLDER = '/code/flask-test/upload_files'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def hello(name=None):
    
    return render_template('hello.html', name=name)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
#            filename = secure_filename(file.filename)
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file'))
        else:
            return '''
            <!doctype html>
            <title>Upload new File</title>
            <h1>File Select Error!</h1>
            <a href="/file">file</a>
            '''
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route("/user/<username>")
def profile(username):
    return u"こんにちは！"+username+u"くん！"

if __name__ == "__main__":
    app.run(debug=True)
