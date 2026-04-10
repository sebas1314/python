from flask import Flask, jsonify, request

app = Flask(__name__)

# Nuestra "Base de datos" temporal (una lista de diccionarios)
clientes = [
    {"id": 1, "nombre": "Santi Vasquez", "email": "santi@mail.com"},
    {"id": 2, "nombre": "Admin", "email": "admin@python.com"}
]

# 1. LEER TODO (Read All)
@app.route('/clientes', methods=['GET'], strict_slashes=False)
def obtener_clientes():
    return jsonify(clientes)

# 2. CREAR (Create)
@app.route('/clientes', methods=['POST'], strict_slashes=False)
def agregar_cliente():
    datos = request.get_json()
    if isinstance(datos, list): datos = datos[0] # Por si mandas una lista por error
    
    nuevo_cliente = {
        "id": len(clientes) + 1,
        "nombre": datos.get('nombre', 'Sin Nombre'),
        "email": datos.get('email', 'Sin Email')
    }
    clientes.append(nuevo_cliente)
    return jsonify({"mensaje": "Cliente creado", "cliente": nuevo_cliente}), 201

# 3. ACTUALIZAR (Update)
@app.route('/clientes/<int:id>', methods=['PUT'])
def actualizar_cliente(id):
    for cliente in clientes:
        if cliente['id'] == id:
            cliente['nombre'] = request.json.get('nombre', cliente['nombre'])
            cliente['email'] = request.json.get('email', cliente['email'])
            return jsonify({"mensaje": "Cliente actualizado", "cliente": cliente})
    return jsonify({"error": "No encontrado"}), 404

# 4. ELIMINAR (Delete)
@app.route('/clientes/<int:id>', methods=['DELETE'])
def eliminar_cliente(id):
    global clientes
    clientes = [c for c in clientes if c['id'] != id]
    return jsonify({"mensaje": "Cliente eliminado"})

if __name__ == '__main__':
    print("Servidor CRUD iniciado en http://127.0.0.1:5000/clientes")
    app.run(debug=True)
