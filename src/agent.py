from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
import os
from dotenv import load_dotenv
from src.tools import time, creators, whoami, search

load_dotenv()

model = ChatOpenAI(
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model_name="amazon/nova-2-lite-v1:free",
    temperature=0.4,
    streaming=True,
)

agent = create_agent(model, tools=[time, creators, whoami, search])
