from fastapi import FastAPI
import os

app = FastAPI()

@app.get('/')
def home():
    return {'Hello': 'this is home page'}

@app.get('/health')
def health():
    return {'status':'ok'}

if __name__=='__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8080)), reload=True)