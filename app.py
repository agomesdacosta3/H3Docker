from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello welcome in the app.\n'
