from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle
from description.llm_chain import description_chain

app = FastAPI()

# Load pipeline (transformer + model)
with open("zameen_model.pkl", "rb") as f:
    pipeline = pickle.load(f)

class HouseData(BaseModel):
    property_type: str
    location: str
    city: str
    baths: int
    purpose: str
    bedrooms: int
    area_type: str    # lowercase with underscores
    area_size: float


@app.post("/predict/")
def predict(data: HouseData):
    print("[DEBUG] Incoming data:", data)

    # Convert input to DataFrame
    input_df = pd.DataFrame([data.dict()])

    # ✅ Only rename the 2 columns that differ from training
    input_df.rename(columns={
        "area_type": "Area Type",
        "area_size": "Area Size"
    }, inplace=True)

    print("[DEBUG] Columns after renaming:", input_df.columns.tolist())

    # Predict price
    price = pipeline.predict(input_df)[0]
    print(f"[DEBUG] Predicted price: {price}")

    # Generate description (no renaming needed for LLM)
    description = description_chain.invoke({
        "property_type": data.property_type,
        "location": data.location,
        "city": data.city,
        "bedrooms": data.bedrooms,
        "baths": data.baths,
        "area_size": data.area_size,
        "area_type": data.area_type,
        "purpose": data.purpose
    })

    return {
        "predicted_price": round(price, 2),
        "description": description.content
    }



