import os
from flask import Flask, jsonify, render_template
from flask_cors import CORS
from prometheus_flask_exporter import PrometheusMetrics, Counter

template_directory = os.path.abspath('src/templates')
static_directory = os.path.abspath('src/static')

app = Flask(__name__, template_folder=template_directory,
            static_folder=static_directory)
CORS(app)

metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version='1.0')

counter = Counter('requests_total', 'Total number of requests')


@app.route('/metrics')
def metrics():
    counter.inc()
    return metrics.metrics, 200


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_url', methods=['GET'])
def get_url():
    hardcoded_url = "https://www.google.com"
    return jsonify({"url": hardcoded_url})


HOST = '0.0.0.0'
# 192.168.0.106
# 130.229.178.24
if __name__ == '__main__':
    app.run(host=HOST, port=8080)
