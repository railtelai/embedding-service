from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from server.controllers import router as EmbeddingController

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(EmbeddingController,prefix="/api/v1")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=2000)
