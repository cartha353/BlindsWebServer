from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blinds/<function>')
def openBlinds(function):
    return render_template('blinds.html', function=function)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')