from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
import models



app = Flask(__name__)  # create a flask app named flask

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5433/mtnusers'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db= SQLAlchemy(app)








@app.route("/")
def home():
    return '''My name is Blouwatito Agboola. This is my CA2 work. My GitHub URL is https://github.com/boluagboola '''

@app.route("/MTN")
def hello2():
    return render_template('home.html', title="Home")



@app.route('/Registered-Users')
def Registered_Users():
    session['next_url'] = request.args.get('next', '/')
    return render_template('welcome.html', title="REGISTERED USERS", information="Enter login details")







@app.route("/signup/")
def signup():
 return render_template('signup.html', title="SIGN UP", information="Use the form displayed to register")

@app.route("/process-signup/", methods=['POST'])
def process_signup():
 firstname = request.form['firstname']
 surname = request.form['surname']
 residentialaddress = request.form['residentialaddress']
 dateofbirth = request.form['dateofbirth']
 nationality = request.form['nationality']
 nationalidentificationnumber = request.form[ 'natioinalidentificationnumber']
 # let's write to the database
 try:
    user = models.User(firstname=firstname, surname=surname, residentialaddress=residentialaddress, dateofbirth=dateofbirth, nationality=nationality, nationalidentificationnumber= nationalidentificationnumber)
    db.session.add(user)
    db.session.commit()

 except Exception as e:
    # Error caught, prepare error information for return
    information = 'Could not submit. The error message is {}'.format(e.__cause__)
    return render_template('Registration.html', title="REGISTER", information=information)


 information = 'User by name {} {} successfully added. The login name is the email address {}.'.format(firstname, surname, nationalidentificationnumber)

 return render_template('Registration.html', title="REGISTER", information=information)






if __name__ == "__main__":
    app.run(port= 5005)
