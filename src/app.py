from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template("home.html")
    
@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/quemsomos")
def quemsomos():
    return render_template("quemsomos.html")
    
if __name__ == "__main__":
    app.run(debug=True)

    ###  from _main_ import app from flask_mysqldb import MySQL myql=MySQL(app)