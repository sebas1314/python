from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def inicio():
    return jsonify({
        "mensaje": "¡Hola! Esta es tu primera API",
        "usuario": "sebas1314",
        "estado": "Conectado"
    })

@app.route('/saludo/<nombre>')
def saludar(nombre):
    return jsonify({
        "saludo": f"Hola {nombre}, ¿cómo estás?",
        "id": 1
    })

if __name__ == '__main__':
    print("Iniciando el servidor en http://127.0.0.1:5000")
    app.run(debug=True)
