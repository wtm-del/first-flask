from flask import Flask, render_template
app = Flask(__name__)

@app.route("/another")
def show():
    return '<h1>Yo</h1>'

@app.route('/user/<username>')
def insert(username):
    return f"Hi {username[2]}"

@app.route("/")
def index():
    signed_in = False
    return render_template('index.html', signed_in=signed_in)

if __name__ == '__main__': # Revisit previous challenge if you're uncertain what this does https://code.nextacademy.com/lessons/name-main/424
   app.run(debug=True)