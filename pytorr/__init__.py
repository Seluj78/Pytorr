from flask import Flask

application = Flask(__name__)


@application.route("/")
def home():
    return "Welcome to Pytorr!"
