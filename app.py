from flask import Flask

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/")
def home():
    return "Hello, DevOps!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
