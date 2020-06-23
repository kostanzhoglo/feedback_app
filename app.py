from flask import Flask, render_template, request
# start to implement the database
from flask_sqlalchemy import SQLAlchemy
# os and dotenv are so I can access the env variables in this project for pgAdmin
import os
from dotenv import load_dotenv

load_dotenv()
OWNER = os.getenv('OWNER')
DB_PASSWORD = os.getenv('DB_PASSWORD')


# initialize our app
app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://' + str(OWNER) + ':' + str(DB_PASSWORD) + '@localhost/lexus'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer(200))
    comments = db.Column(db.Text())
    

# Make a route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        # print(customer, dealer, rating, comments)
        if customer == '' or dealer == '':
            return render_template('index.html', message='Please enter customer and dealer fields.')
        return render_template('success.html')


if __name__ == '__main__':
    ## set debug to True when in development. Lets server keep reloading when we make changes.
    # Place this up above in the if ENV clause...
    # app.debug = True
    app.run()