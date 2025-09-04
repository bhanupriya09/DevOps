
from flask import Flask, jsonify, request

def create_app():
    app = Flask(__name__)

    @app.get("/")
    def index():
        return jsonify({
            "app": "ACEest Fitness & Gym API",
            "version": "1.0.0",
            "message": "Welcome to ACEest Fitness & Gym API"
        })

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    @app.post("/bmi")
    def bmi():
        data = request.get_json(silent=True) or {}
        if "weight_kg" not in data or "height_cm" not in data:
            return jsonify({"error": "weight_kg and height_cm are required"}), 400
        try:
            weight = float(data["weight_kg"])
            height_cm = float(data["height_cm"])
        except (TypeError, ValueError):
            return jsonify({"error": "weight_kg and height_cm must be numbers"}), 400
        if weight <= 0 or height_cm <= 0:
            return jsonify({"error": "weight_kg and height_cm must be positive"}), 400

        height_m = height_cm / 100.0
        bmi_value = weight / (height_m ** 2)

        if bmi_value < 18.5:
            category = "underweight"
        elif bmi_value < 25:
            category = "normal"
        elif bmi_value < 30:
            category = "overweight"
        else:
            category = "obese"

        return jsonify({
            "bmi": round(bmi_value, 2),
            "category": category
        }), 200

    return app

# WSGI entrypoint for gunicorn
app = create_app()

if __name__ == "__main__":
    # Local dev server (debug)
    app.run(host="0.0.0.0", port=5000, debug=True)
