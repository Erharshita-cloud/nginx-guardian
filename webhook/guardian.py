from prometheus_client import start_http_server, Counter, Gauge

failures_total = Counter("guardian_failures_total", "Number of failures detected")
restarts_total = Counter("guardian_restarts_total", "Number of recovery attempts")
status_gauge = Gauge("guardian_status", "Current nginx status (1=up,0=down)")

def start_metrics():
    start_http_server(9101)
    print("[guardian] Metrics available on :9101/metrics")
