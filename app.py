# from sre_constants import SUCCESS
from flask import Flask, render_template, request
from pip import main
from second import second
from second1 import second1
from sqlalchemy import false, true
from flask_mail import Mail, Message
from config import mail_username, mail_password
from sqlalchemy import true
import os
from flask_sqlalchemy import SQLAlchemy
import pickle
import sqlite3
import os

# currentlocation = os.path.dirname(os.pathe.abspath(__file__))

app = Flask(__name__)

app.register_blueprint(second,url_prefix="")
app.register_blueprint(second1,url_prefix="")


app.config['MAIL_SERVER'] = "smtp-mail.outlook.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSl'] = False
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password


mail = Mail(app)

# @app.route("/", methods = ['GET'])
@app.route("/index")
def HomePage():
    return render_template('index.html')   

@app.route("/contactForm", methods = ['GET' , 'POST'])
def contactForm():
    if request.method == "POST":
        name = request.form.get('Name')
        email = request.form.get('Email')
        phone = request.form.get('Phone')
        message = request.form.get('Message')

        msg = Message(subject=f"Mail from{name}", body=f"Name: {name}\nE-Mail: {email}\nPhone: {phone}\n\n\n{message}", sender=mail_username, recipients=['oppanchayat5@gmail.com'])
        mail.send(msg)
        return render_template("contactForm.html", success=True)

    return render_template('contactForm.html')


@app.route("/services")
def services():
    return render_template('services.html')   


@app.route("/aboutus")
def aboutUs():
    return render_template('aboutUs.html')    

@app.route("/login", )
def login():
    return render_template('login.html')   
database = {'akshit':'123654','vedant':'654789','shweta':'789654'}

@app.route('/dashboard', methods=['POST', 'GET'] )
def dashboard():
    if request.method == "POST" :
        name1 = request.form['username1']
        pwd = request.form['password1']

    # sqlconnection = sqlite3.Connection(currentlocation + "./login.db")
    # cursor = sqlconnection.cursor()
    # query1 = "SELECT username, password from Users WHERE username = '{un}' AND password = '{pw}'".format(un = name1, pw = pwd)

    # rows = cursor.execute(query1)
    # rows = rows.fetchall()
    # if len(rows) == 1:
    #     return render_template('login.html')

        if name1 not in database:
            return render_template('login.html', info ='Invalid User')
        else:
            if database[name1]!=pwd:
                return render_template('login.html', info = "Invalid Password")
            else:
                return render_template('dashboard.html', name = name1)  

if __name__ == '__main__':
    app.run(debug=true,port = 112)
