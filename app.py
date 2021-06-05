from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Current position'

@app.route('/open')
def cakes():
    return 'Open Blinds'

@app.route('/close')
    return 'Close Blinds'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')