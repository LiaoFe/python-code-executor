from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import dotenv
from pyston import PystonClient, File
import asyncio
import numpy as np
import nest_asyncio

dotenv.load_dotenv()
app = FastAPI()
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Code(BaseModel):
    code: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/execute")
async def execute(code: Code):
    outputs = []
    async def main():
        client = PystonClient()
        
        output = await client.execute("python", [File(code.code)])
        print(output)
        outputs.append(output)

    loop = nest_asyncio.apply(await main())
    # await loop.run_until_complete(await main())
    
    return outputs
