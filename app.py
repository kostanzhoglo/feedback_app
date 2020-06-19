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
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        # print(customer, dealer, rating, comments)
        if customer == '' or dealer == '':
            return render_template('index.html', message='Please enter customer and dealer fields.')
        return render_template('success.html')


if __name__ == '__main__':
    # set debug to True when in development. Lets server keep reloading when we make changes.
    app.debug = True
    app.run()