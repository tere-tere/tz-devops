from flask import Flask, render_template
from os import getenv
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


if __name__ == '__main__':
    port = int(getenv("PORT", 8080)) #создали переменную в докере
    app.run(host="0.0.0.0",port=port) #host 127...