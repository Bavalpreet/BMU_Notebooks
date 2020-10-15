from flask import Flask,redirect,render_template ,url_for,request,flash
app = Flask(__name__)  
app.secret_key = "abc"  
 
@app.route('/index')  
def home():  
    return render_template("index.html")  
 
@app.route('/login',methods = ["GET","POST"])  
def login():  
    error = None
    if request.method == "POST":  
        if request.form['pass'] != 'jtp':  
            error = "invalid password"  
        else:  
            flash("you are successfuly logged in")
            # you can enter multiple flash messages here
            flash("Welcome to the guest room")  
            return redirect(url_for('home'))  
    return render_template('login.html',error=error)  
  
      
if __name__ == '__main__':  
    app.run(debug = True)  