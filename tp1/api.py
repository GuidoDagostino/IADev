from flask import Flask, jsonify, request

from models.persona import Persona
from services.persona_service import PersonaService


app = Flask(__name__)

# Un único servicio para toda la app: si se creara uno por request,
# el repositorio en memoria se reiniciaría y el POST no quedaría guardado.
servicio = PersonaService()


def persona_a_json(persona: Persona) -> dict:
    return {
        "dni": persona.dni,
        "nombre": persona.nombre
    }


@app.get("/persona")
def obtener_personas():
    personas = servicio.obtener_personas()

    return jsonify([persona_a_json(persona) for persona in personas])


@app.get("/persona/<int:dni>")
def obtener_persona(dni):
    persona = servicio.obtener_persona_por_dni(dni)

    if persona is None:
        return jsonify({
            "error": "Persona no encontrada"
        }), 404

    return jsonify(persona_a_json(persona))


@app.post("/persona")
def agregar_persona():
    datos = request.get_json(silent=True)

    if not datos or "dni" not in datos or "nombre" not in datos:
        return jsonify({
            "error": "El body debe tener 'dni' y 'nombre'."
        }), 400

    try:
        persona = Persona(datos["dni"], datos["nombre"])
    except ValueError as error:
        return jsonify({
            "error": str(error)
        }), 400

    try:
        servicio.agregar_persona(persona)
    except ValueError as error:
        return jsonify({
            "error": str(error)
        }), 409

    return jsonify(persona_a_json(persona)), 201


if __name__ == "__main__":
    app.run(debug=True)
