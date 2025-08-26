from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from utils.ocr import extract_text
from recommendation import generate_recommendation

app = FastAPI()

# Allow all origins for simplicity; update for production use
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_chart(file: UploadFile = File(...)):
    """Analyze an uploaded trading chart image and return a recommendation."""
    content = await file.read()
    text = extract_text(content)
    # Choose symbol based on text content; this is just an example
    symbol = "BTC/USDT" if "BTC" in text else "ETH/USDT"
    result = generate_recommendation(symbol)
    return result
