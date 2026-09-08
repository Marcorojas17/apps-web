# apps/live.py - KRONOS 28 ITZA - Backend Cimático
from flask import Flask, send_from_directory, jsonify, request
import os

app = Flask(__name__, static_folder='web')

WEB_DIR = os.path.join(os.path.dirname(__file__), 'web')

@app.route('/')
def index():
    return send_from_directory(WEB_DIR, 'index.html')

@app.route('/live')
@app.route('/live.html')
def live():
    return send_from_directory(WEB_DIR, 'live.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(WEB_DIR, path)

@app.route('/api/status')
def status():
    return jsonify({
        "system": "KRONOS 28 ITZA",
        "module": "Cymatic Visualizer",
        "status": "online",
        "version": "Premium Elite",
        "endpoints": ["/", "/live", "/api/analyze"]
    })

@app.route('/api/analyze', methods=['POST'])
def analyze():
    # Aquí enlazas tu lógica Python de frecuencias si quieres procesar audio en backend
    data = request.get_json() or {}
    freq = data.get('freq', 0)
    # Ejemplo: clasificación por banda KRONOS
    if freq < 150: band = "KRONOS Bass - Morado"
    elif freq < 350: band = "Blue Icy - Elite Strategist"
    elif freq < 700: band = "Gold Chromatic - Premium Elite"
    else: band = "Red - High Frequency"
    return jsonify({"freq": freq, "band": band, "symmetry": max(3, min(12, round(3 + freq/200)))})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)