from flask import Flask, render_template
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUESTS = Counter('app_requests_total', 'Total HTTP requests')

@app.route('/')
def index():
    REQUESTS.inc()
    return render_template('index.html')

@app.route('/about')
def about():
    REQUESTS.inc()
    return "<h1>About this sample app</h1><p>Simple Flask app for DevOps practice.</p>"

# Prometheus metrics endpoint (optional)
@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

