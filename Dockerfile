FROM python:3.11 AS runtime

WORKDIR /app

COPY requirements.txt .
RUN [ "pip", "install", "-r", "requirements.txt" ]

FROM runtime AS builder

COPY build_model.py .
COPY houses.csv .
RUN [ "python", "build_model.py" ]

FROM runtime

COPY model_dashboard.py .
COPY --from=builder /app/regression.joblib .

CMD [ "streamlit", "run", "model_dashboard.py" ]
