FROM python:3.13-slim AS builder
WORKDIR /app

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock* ./
RUN uv pip install --system -r pyproject.toml --no-cache-dir

COPY . .

FROM python:3.13-slim AS runtime
WORKDIR /app

COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

COPY --from=builder /app /app

RUN useradd -m -u 1000 appuser && chown -R 1000:1000 /app
USER 1000

EXPOSE 8000

ENTRYPOINT ["python", "app.py"]