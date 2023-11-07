import os
import json
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

from constants import DESCRIPTION

class InputData(BaseModel):
    prompt: str

class OutputData(BaseModel):
    response: str

class Configs:

    with open("configs.json", 'r') as f:
        data = json.load(f)
        f.close()

    API_KEY = data["api_key"]
    MODEL = data['model']
    VERSION = data['version']

class Server(Configs):
   
    os.environ["OPENAI_API_KEY"] = Configs().API_KEY
    client = OpenAI()

    def __init__(self):
        super().__init__()

    def create_app(self):
        return FastAPI(
            title=f"Inference API for {self.MODEL.upper()}",
            description=DESCRIPTION,
            version=f"{self.VERSION}",
        )

    def get_chat_response(self, prompt):
        response = self.client.chat.completions.create(
            model=self.MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content