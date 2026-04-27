FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    ffmpeg \
    gcc \
    g++ \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN mkdir -p /root/.cache/torch/hub/checkpoints/

COPY models/955717e8-8726e21a.th /root/.cache/torch/hub/checkpoints/

RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

CMD python -m demucs.separate -d cpu lp_numb_test.wav && python compare.py