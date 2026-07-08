from pydantic import BaseModel, Field
from typing import Optional, List

class OrderQuery(BaseModel):
    order_id: Optional[str] = Field(None, description="The unique alphanumeric ID of the order (e.g., ORD-1001).")
    status: Optional[str] = Field(None, description="Filter orders by status: Pending, Shipped, Delivered, Cancelled.")

class OrderItem(BaseModel):
    item_name: str
    quantity: int
    price: float

class OrderDetails(BaseModel):
    order_id: str
    customer_id: int
    items: List[OrderItem]
    total_amount: float
    status: str
    estimated_delivery: Optional[str] = None

class OrderResponse(BaseModel):
    status: str
    results: List[OrderDetails]