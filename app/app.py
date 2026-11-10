
from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
from opentelemetry import trace
from opentelemetry import trace as otel_trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
import logging
import os
import time

app = Flask(__name__)

# Prometheus metrics
metrics = PrometheusMetrics(app)
metrics.info("application_info", "Application information", version="1.0.0")

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s"
)

logger = logging.getLogger("observability-app")

# OpenTelemetry tracing configuration
resource = Resource.create({
    "service.name": "observability-flask-app"
})

provider = TracerProvider(resource=resource)

otlp_exporter = OTLPSpanExporter(
    endpoint=os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "http://jaeger:4317"),
    insecure=True
)

provider.add_span_processor(BatchSpanProcessor(otlp_exporter))
trace.set_tracer_provider(provider)

FlaskInstrumentor().instrument_app(app)

tracer = otel_trace.get_tracer(__name__)


@app.route("/")
def home():
    logger.info("Home endpoint accessed")

    with tracer.start_as_current_span("home-operation"):
        return jsonify({
            "message": "Welcome to Observability Project",
            "status": "running"
        })


@app.route("/health")
def health():
    logger.info("Health check requested")

    return jsonify({
        "status": "healthy"
    }), 200


@app.route("/work")
def work():
    logger.info("Work endpoint processing request")

    with tracer.start_as_current_span("work-operation"):
        time.sleep(0.5)

        return jsonify({
            "message": "Work completed successfully",
            "status": "success"
        })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

