from flask import Flask, render_template
from blueprints.auth.views import bp as bp_auth

app = Flask(__name__)
app.secret_key = 'qwerty123'
app.debug = True

@app.route('/')
def home():
    return render_template('home.html')

app.register_blueprint(bp_auth)
