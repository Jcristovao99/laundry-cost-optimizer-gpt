
from fastapi import FastAPI
from pydantic import BaseModel
from optimizer import optimize_order

app = FastAPI()

class Order(BaseModel):
    items: dict
    delivery_location: str = "default"

@app.post("/optimize")
def optimize(order: Order):
    total, breakdown, _ = optimize_order(
        order.items, order.delivery_location
    )
    return {"total_cost": total, **breakdown}
