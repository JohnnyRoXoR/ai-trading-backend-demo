# AI Trading Backend Demo

This repository contains a simple FastAPI backend for analyzing cryptocurrency chart images and generating basic trading recommendations. It demonstrates how to upload chart screenshots, extract text via OCR and produce simple long/short/hold suggestions.

## Features

- **Upload an image** of a trading chart (PNG/JPEG).
- **Extract text** from the image using Tesseract OCR.
- **Determine the trading symbol** (BTC/USDT or ETH/USDT) from the extracted text.
- **Generate a random trading recommendation** (Long/Short/Hold) with entry and exit prices and confidence score.

This demo is intended as a starting point for building more sophisticated AI-powered trading assistants.

## Endpoints

- `POST /analyze` – Upload a chart image. Returns a JSON with a trading recommendation.

## Usage

Install the dependencies:

```
pip install -r requirements.txt
```

Run the server locally:

```
uvicorn main:app --reload
```

Once running, send a POST request with a chart file:

```
curl -X POST -F "file=@chart.png" http://localhost:8000/analyze
```

The response will contain a randomly generated recommendation:

```
{
  "symbol": "BTC/USDT",
  "confidence": 90,
  "recommendation": "Long",
  "entry": 49500,
  "exit": 51000
}
```

## Disclaimer

This project is for demonstration purposes only. The recommendations are random and **should not** be used for actual trading decisions.
