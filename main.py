from fastapi import FastAPI
from pydantic import BaseModel
from utils import generate_description
#from utils import generate_description
# Initialize FastAPI
app = FastAPI()

# Define your data model for Product

class Product(BaseModel):
    #name: str
    notes: str

@app.post("/ESG")
async def generate_product_description(product: Product):
    description = generate_description(f"Notes: {product.notes}")
    return {"답변": description}

#uvicorn main:app --reload