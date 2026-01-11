from flask import Flask, jsonify
import psycopg2
import os
import time

app = Flask(__name__)

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


# ---------------- HEALTH ENDPOINT ----------------
@app.route("/health")
def health():
    start_time = time.time()

    api_status = "Healthy"
    db_status = "Healthy" if check_database() else "Unhealthy"

    total_time = round(time.time() - start_time, 2)

    return jsonify({
        "status": "Healthy" if api_status == "Healthy" and db_status == "Healthy" else "Unhealthy",
        "totalDuration": f"0:00:{total_time}",
        "entries": {
            "apiHealthCheck": {
                "description": "The API is healthy",
                "status": api_status
            },
            "dbHealthCheck": {
                "description": "The database is up and running" if db_status == "Healthy" else "Database connection failed",
                "status": db_status
            }
        }
    })


# ---------------- MAIN ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
