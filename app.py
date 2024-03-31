from flask import Flask, render_template
from Ventana import formulario

app = Flask(__name__)

@app.route("/getClientes",methods=['GET'])

def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()