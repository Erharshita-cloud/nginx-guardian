from flask import Flask, request
import subprocess
import datetime

app = Flask(__name__)

NGINX_CONTAINER = "self_healing_nginx"

def is_nginx_running():
    result = subprocess.run(
        ["docker", "inspect", "-f", "{{.State.Running}}", NGINX_CONTAINER],
        capture_output=True, text=True
    )
    return result.stdout.strip() == "true"

def restart_nginx():
    subprocess.run(["docker", "restart", NGINX_CONTAINER])

@app.route('/', methods=['GET', 'POST'])
def alert():
    if request.method == 'POST':
        # Get JSON payload or fallback
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form.to_dict() or {}

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        source_ip = request.remote_addr
        print(f"[{now}] Received alert from {source_ip}: {data}")

        # Self-healing: restart NGINX if down
        if not is_nginx_running():
            print(f"[{now}] NGINX container is down! Restarting...")
            restart_nginx()
            print(f"[{now}] NGINX restarted successfully.")
        else:
            print(f"[{now}] NGINX container is running normally.")

        return '', 200
    else:
        # Handle GET requests for health check
        return "Webhook is running", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

