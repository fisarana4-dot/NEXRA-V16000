from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
trace.set_tracer_provider(TracerProvider())
s=trace.get_tracer('nexra').start_span('order')
