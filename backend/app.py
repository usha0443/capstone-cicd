from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# ---------------- ROOT (OPTIONAL, FOR BROWSER) ----------------
@app.route("/")
def home():
    return jsonify({
        "message": "Backend is running"
    }), 200


# ---------------- DATABASE CHECK ----------------
def check_database():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            connect_timeout=2
        )
        conn.close()
        return True
    except Exception:
        return False


# ---------------- APP HEALTH (FOR CI / TESTS) ----------------
@app.route("/health")
def health():
    # ONLY check app is running
    return jsonify({"status": "UP"}), 200


# ---------------- DATABASE HEALTH ----------------
@app.route("/health/db")
def db_health():
    if check_database():
        return jsonify({
            "status": "UP",
            "description": "Database connection successful"
        }), 200
    else:
        return jsonify({
            "status": "DOWN",
            "description": "Database connection failed"
        }), 500


# ---------------- MAIN ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
