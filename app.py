import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="ShopIQ Backend", version="1.0.0")

# Request Data Structure for E-commerce Session Behavior
class CustomerData(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    feature4: float

@app.get("/")
def read_root():
    return {"message": "Welcome to ShopIQ E-commerce Prediction & Segmentation API"}

@app.post("/analyze")
def analyze_customer(data: CustomerData):
    try:
        # Mock intelligence logic for customer purchase prediction & segmentation
        score = (data.feature1 * 0.5) + (data.feature2 * 0.3) + (data.feature3 * 0.2)
        segment = "High-Value Intent" if score > 50 else "Standard Browsing"
        
        return {
            "status": "success",
            "predicted_purchase_probability": round(score / 100, 2),
            "assigned_segment": segment,
            "message": "Customer behavioral analysis completed successfully."
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))