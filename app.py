from flask import Flask, render_template, request,redirect, url_for,flash,session

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/text_send', methods=['POST'])
def send():
    if request.method == 'POST':
        text = request.form['text']
        return render_template('index.html', text=text)


if __name__ == "__main__":
    app.run(port= 3000, debug=True)