from flask import Flask, render_template, request

# initialize our app
app = Flask(__name__)

# Make a route
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == 'main':
    # set debug to True when in development. Lets server keep reloading when we make changes.
    app.debug = True
    app.run()