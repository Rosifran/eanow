"""
E Agora? — API
================
Endpoints simples para a interface web consumir.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, request, jsonify, send_from_directory
from core.matching_engine import MatchingEngine, UserProfile

app = Flask(__name__, static_folder="../web/static")
engine = MatchingEngine()


@app.route("/")
def index():
    return send_from_directory("../web", "index.html")


@app.route("/api/analyze", methods=["POST"])
def analyze():
    """
    Recebe perfil da usuária, devolve análise completa.
    POST body: { trigger, situation, has_reserve, monthly_amount, age? }
    """
    data = request.get_json()

    try:
        profile = UserProfile(
            trigger        = data.get("trigger", "sobra_mensal"),
            situation      = data.get("situation", "estabilidade"),
            has_reserve    = bool(data.get("has_reserve", False)),
            monthly_amount = float(data.get("monthly_amount", 0)),
            age            = int(data["age"]) if data.get("age") else None,
        )
    except (ValueError, TypeError) as e:
        return jsonify({"error": f"Dados inválidos: {e}"}), 400

    analysis = engine.build_analysis(profile)
    return jsonify(analysis)


@app.route("/api/concepts", methods=["GET"])
def concepts():
    """Devolve glossário completo."""
    from data.research_data import CONCEPTS
    return jsonify(CONCEPTS)


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "version": "0.1.0"})


if __name__ == "__main__":
    app.run(debug=True, port=5050)
