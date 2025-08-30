# Importando Flask y render_template
from flask import Flask, render_template

# Creando la app
app = Flask(__name__)

# Contador global
contador = 0

# Ruta principal
@app.route("/")
def index():
    return render_template("index.html", contador=contador)

# Ruta para sumar
@app.route("/sumar")
def sumar():
    global contador
    contador += 1
    return render_template("snippet.html", contador=contador)

# Ejecutar la app
if __name__ == "__main__":
    app.run(debug=True)
