from datetime import datetime
from langchain.tools import tool
from src.index import index


@tool
def time():
    """
    Get current time and date
    Returns:
        str: current date and time string
    """
    return f"Current date and time:{datetime.now()}"


@tool
def whoami():
    """
    Information about you (agent) on how you should present yourself if asked
    Returns:
        str: self description/introduction
    """
    return "He who knows other is wise. He who knows himself is enlightened"


@tool
def creators():
    """
    Information about creators
    Returns:
        str: github nicknames
    """
    return "ML: sxvxmx"


@tool(description="Query the database for relevant items")
def search(query: str):
    """
    Param:
        query: string to create embedding from.
    Desc:
        Get information from files from vector database.
    Returns:
        str: top 3 relevant items in database
    """

    query_engine = index.as_query_engine(similarity_top_k=3, response_mode="no_text")
    return str(query_engine.query(f"{query}").source_nodes)
