from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# Simulerad data
simulation_time = 10  # timmar
total_consumption = 5  # kWh
battery_charge_kwh = 50  # kWh

@app.route('/')
def index():
    """Visa HTML-sidan från static-mappen."""
    return send_from_directory(os.path.join(app.root_path, 'static'), 'index.html')

@app.route('/info', methods=['GET'])
def get_info():
    """Hämta simuleringstid och batteristatus."""
    return jsonify({
        "simulation_time": simulation_time,
        "total_consumption": total_consumption,
        "battery_charge_kwh": battery_charge_kwh
    })

@app.route('/charge', methods=['POST'])
def charge():
    """Hantera laddning av batteriet."""
    data = request.get_json()
    command = data.get("command", "")
    if command == "start":
        return jsonify({"status": "Laddning startad"})
    elif command == "stop":
        return jsonify({"status": "Laddning stoppad"})
    else:
        return jsonify({"error": "Ogiltigt kommando"}), 400

@app.route('/baseload', methods=['GET'])
def get_baseload():
    """Hämta hushållets energiförbrukning."""
    return jsonify({"baseload": 3.5})  # Exempelvärde: 3.5 kWh

@app.route('/priceperhour', methods=['GET'])
def get_prices():
    """Hämta elpriser per timme."""
    hourly_prices = [0.1, 0.15, 0.2, 0.25]  # Exempelpriser
    return jsonify({"prices": hourly_prices})

@app.route('/discharge', methods=['POST'])
def discharge():
    """Hantera urladdning av batteriet."""
    global battery_charge_kwh
    battery_charge_kwh = 10  # Exempel: sätter batterinivån till 10 kWh (20% laddning)
    return jsonify({"status": "Batteri urladdat till 20%"})

if __name__ == '__main__':
    app.run(debug=True)
