import os
from fastapi import Request
from utils import InputData, OutputData, Server

# initiate App
server = Server()
app = server.create_app()

# check health
@app.get("/health")
async def check_health():
    return {"response": "healthy"}

# post
@app.post("/GPT/", response_model=OutputData)
async def get_response(request: Request, input_data: InputData):
    prompt = input_data.prompt
    response = server.get_chat_response(prompt)
    return OutputData(response=response)
