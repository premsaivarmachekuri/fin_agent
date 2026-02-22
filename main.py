import uvicorn
from app.api.v1.routes import router
from fastapi import FastAPI

app = FastAPI(title="Fin Agent", version="0.1.0")
app.include_router(router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
