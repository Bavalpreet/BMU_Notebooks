from flask import *  
from flask_mail import *  
  
app = Flask(__name__)  
  
app.config["MAIL_SERVER"]='smtp.gmail.com'  
app.config["MAIL_PORT"] = 465  
app.config["MAIL_USERNAME"] = 'bavalpreet.singh25@gmail.com'  
app.config['MAIL_PASSWORD'] = 'baval@26'  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  
  
users = [{'name':'syed','email':'syed.aliaryanrizvi.18cse@bmu.edu.in'},{'name':'sai','email':'saiteja23999@gmail.com'},{'name':'indradhar','email':'indradhar.paka.18mec@bmu.edu.in'}]  
  
mail = Mail(app)  
 
@app.route("/")  
def index():  
    with mail.connect() as con:  
        for user in users:  
            message = "hello %s" %user['name']  
            msgs = Message(recipients=[user['email']],body = message, subject = 'hello', sender = 'bavalpreet.singh25@gmail.com')  
            con.send(msgs)  
    return "Sent"  
if __name__ == "__main__":  
    app.run(debug = True)