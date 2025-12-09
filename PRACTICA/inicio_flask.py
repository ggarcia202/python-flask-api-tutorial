from flask import Flask, request, jsonify
app = Flask(__name__) 


# Lista inicial de personas con más detalles
persons = [
    {"name": "Alice", "age": 30, "city": "New York", "occupation": "Engineer", "hobbies": ["Reading", "Traveling", "Swimming"], "otro": {"subkey": "subvalue"} },
    {"name": "Bob", "age": 25, "city": "Los Angeles", "occupation": "Designer", "hobbies": ["Drawing", "Cycling", "Hiking"]},
    {"name": "Charlie", "age": 35, "city": "Chicago", "occupation": "Teacher", "hobbies": ["Cooking", "Gardening", "Photography"]},
    {"name": "Diana", "age": 28, "city": "Miami", "occupation": "Doctor", "hobbies": ["Yoga", "Dancing", "Traveling"]},
    {"name": "Ethan", "age": 32, "city": "Seattle", "occupation": "Developer", "hobbies": ["Gaming", "Reading", "Running"]},
]

print(f"{persons[0]['name']}, {persons[0]['otro']['subkey']}")  # Acceder a un valor dentro de un diccionario anidado


# Ruta de inicio que sirve un formulario HTML simple
@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Crear Persona</title>
    </head>
    <body>
        <h2>Crear Persona</h2>

        <label>Nombre:</label>
        <input type="text" id="name" /><br><br>

        <label>Edad:</label>
        <input type="number" id="age" /><br><br>

        <label>Ciudad:</label>
        <input type="text" id="city" /><br><br>

        <label>Ocupación:</label>
        <input type="text" id="occupation" /><br><br>

        <label>Hobbies (separados por coma):</label>
        <input type="text" id="hobbies" /><br><br>

        <button onclick="enviarPersona()">Enviar Persona</button>

        <script>
            function enviarPersona() {
                const data = {
                    name: document.getElementById("name").value,
                    age: parseInt(document.getElementById("age").value),
                    city: document.getElementById("city").value,
                    occupation: document.getElementById("occupation").value,
                    hobbies: document.getElementById("hobbies").value.split(",").map(h => h.trim())
                };

                fetch('/persons', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                })
                .then(response => response.json())
                .then(result => {
                    alert("Persona añadida: " + JSON.stringify(result));
                })
                .catch(error => console.error("Error:", error));
            }
        </script>
    </body>
    </html>
    """


@app.route("/persons", methods=['POST', 'GET'])
def handle_persons():
    print("\nMétodo de la solicitud:", request.method)
    if request.method == 'POST':
        print("Datos recibidos:", request.get_json())
        data = request.get_json()
        if data['age'] < 18:
            return jsonify({"error": "No se admiten menolsito"}), 400
        
        persons.append(data) # Agregar la nueva persona a la lista
        return jsonify({"message": "Persona añadida exitosamente!", "data": data}), 201

    elif request.method == 'GET':
        return jsonify(persons)


@app.route("/persons/<int:person_id>", methods=['GET'])
def get_person(person_id):
    if 0 <= person_id < len(persons):
        return jsonify(persons[person_id])
    return jsonify({"error": "Persona no encontrada"}), 404


@app.route("/persons/name/<string:person_name>", methods=['GET'])
def get_person_by_name(person_name):
    for person in persons:
        if person["name"].lower() == person_name.lower():
            return jsonify(person)
    return jsonify({"error": "Persona no encontrada"}), 404


# Finalmente iniciamos el servidor en el localhost
app.run(host='0.0.0.0') 
 
