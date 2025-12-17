from src.agent import agent
from langchain_core.messages import HumanMessage, SystemMessage

mode = "System Instruction: Absolute Mode. "
task = (
    "Your task is to be a helpful assistant. Use tools to provide best possible result."
)


def ask_advanced(question: str):
    messages = {
        "messages": [
            SystemMessage(content=mode + task),
            HumanMessage(content=question),
        ]
    }
    for chunk, metadata in agent.invoke(messages, stream_mode="messages"):
        if len(chunk.content_blocks) == 1:
            if "text" in chunk.content_blocks[0].keys():
                yield str(chunk.content_blocks[0]["text"])
