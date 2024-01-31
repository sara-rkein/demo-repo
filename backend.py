from flask import Flask, render_template,request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "index"

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        yourname = request.form['yourname']
        education = request.form['education']
        rating = request.form['rating']
        comments = request.form['comments']

        if yourname == '' or education == '':
            message='Please enter required fields'
            return 'Please enter required fields'
        else: 
            message= yourname +'\n'+ education +"\n"+ rating +"\n" +comments
            return yourname +'\n'+ education +'\n'+ rating +'\n' +comments


@app.route('/hello')
def hello():
    return 'Hello, World'

if __name__ == "__main__":    
  app.debug = True

  app.run(port= 4000)