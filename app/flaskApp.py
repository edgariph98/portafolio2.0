from flask import Flask, render_template, url_for, flash, redirect, request 
import json
from .modules import messageForm
import smtplib  
import os
def sendMSG(senderName,senderEmail,msg):
    email = os.environ.get('EMAIL_USER')
    password = os.environ.get('EMAIL_PASSWORD')
    print(email,password)
    with smtplib.SMTP('smtp.office365.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(email,password)
        subject = "Personal Website Contact Request"
        body = "Name: " +  senderName + ".\n\nEmail: " + senderEmail + ".\n\n" + "Message: \n       " + msg + "\n\n" + "Sincerely,\nYour Mail System Website."
        message = f'Subject:  {subject}\n\n{body}'
        print(message)
        smtp.sendmail(email,'edgar_ivanhdz15@hotmail.com',message)
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'aDm0iW55TDrBldJ6dMbd'
    ########################################
    #          Main Page Route             #
    ########################################
    @app.route('/', methods=['GET','POST'])
    @app.route('/home', methods=['GET','POST'])
    def home():
        msgForm = messageForm()
        if msgForm.validate_on_submit():
            senderEmail = msgForm.email.data
            senderName = msgForm.name.data
            senderMSG = msgForm.message.data
            sendMSG(senderName,senderEmail,senderMSG)
            flash("Message sent to Edgar Portales",'success')
        elif request.method == "POST":
            flash("Conctact form not sent,Please fill out all inputs correctly!")
            print(msgForm.errors)

        return render_template("index.html",form=msgForm)
    return app
if  __name__ == "__main__":

    #create_app().run(debug=True)
    sendMSG("edgar","email@mail.com","Hello")