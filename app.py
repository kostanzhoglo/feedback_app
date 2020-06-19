from flask import Flask, render_template, request

# initialize our app
app = Flask(__name__)

# Make a route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']


if __name__ == '__main__':
    # set debug to True when in development. Lets server keep reloading when we make changes.
    app.debug = True
    app.run()