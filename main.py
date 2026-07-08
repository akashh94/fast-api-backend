from fastapi import FastAPI, status, HTTPException
from schemas import OrderQuery, OrderResponse, OrderDetails
from typing import List
import os

app = FastAPI()

# Mock Orders Database
MOCK_ORDERS = [
    {
        "order_id": "ORD-1001",
        "customer_id": 101,
        "items": [{"item_name": "Mechanical Keyboard", "quantity": 1, "price": 4500.00}],
        "total_amount": 4500.00,
        "status": "Delivered",
        "estimated_delivery": "2026-07-02"
    },
    {
        "order_id": "ORD-1002",
        "customer_id": 101,
        "items": [
            {"item_name": "Type-C Hub", "quantity": 1, "price": 1200.00},
            {"item_name": "Mouse Pad", "quantity": 2, "price": 400.00}
        ],
        "total_amount": 2000.00,
        "status": "Shipped",
        "estimated_delivery": "2026-07-10"
    },
    {
        "order_id": "ORD-1003",
        "customer_id": 102,
        "items": [{"item_name": "Noise Cancelling Headphones", "quantity": 1, "price": 15000.00}],
        "total_amount": 15000.00,
        "status": "Pending",
        "estimated_delivery": "2026-07-14"
    }
]

@app.post("/get-orders", response_model=OrderResponse, status_code=status.HTTP_200_OK)
async def get_orders(payload: OrderQuery):
    """
    Retrieve order details and fulfillment statuses.
    Agents should invoke this tool whenever a customer asks about their order history, tracking information, or specific order items.
    """
    filtered_orders = MOCK_ORDERS
    
    # Filter by specific Order ID if provided
    if payload.order_id:
        filtered_orders = [o for o in filtered_orders if o["order_id"].upper() == payload.order_id.upper()]
        if not filtered_orders:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Order ID {payload.order_id} could not be found."
            )
            
    # Filter by Status if provided
    if payload.status:
        filtered_orders = [o for o in filtered_orders if o["status"].lower() == payload.status.lower()]
        
    return OrderResponse(status="success", results=[OrderDetails(**order) for order in filtered_orders])

@app.get('/')
def home():
    return {'Hello': 'this is home page'}

@app.get('/health')
def health():
    return {'status':'ok'}

@app.get('/greet')
def greet(name: str = 'Guest'):
    """
    General greeting function for agents.
    
    Args:
        name: The name of the person to greet (default: 'Guest')
    
    Returns:
        A greeting message
    """
    return {
        'message': f'Hello, {name}!',
        'name': name,
        'status': 'success'
    }

if __name__=='__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8080)), reload=True)