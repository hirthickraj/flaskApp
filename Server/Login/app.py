
from flask import Flask, render_template, request, url_for, redirect
from flask_pymongo import PyMongo
import re
  
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://instaboy:instaboy@instaboy.hh1km.mongodb.net/userdatabase?retryWrites=true&w=majority&ssl=true&tlsAllowInvalidCertificates=true"
mongo = PyMongo(app)
db = mongo.db.userdata

@app.route('/', methods=('GET', 'POST'))
def register():
    msg = ''
    if request.method == 'POST' and 'firstName' in request.form and 'lastName' in request.form and 'number' in request.form :
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        number = request.form['number']
        print(firstName,lastName,number)
        if len(firstName)<3:
            msg = 'Atlest 3 Characters requied'
        if len(lastName)<3:
            msg='Atleast 3 Characters required'
        if len(number)!=10:
            msg= 'Invalid Mobile Number'
        if not firstName or not lastName or not number:
            msg = 'Please fill out the form !'
        if len(msg)!=0:
            print('Inserting to DB')
            db.insert_one({'firstname':firstName,'lastname':lastName,'number':number})
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html',msg=msg)

if __name__=='__main__':
    app.run()

