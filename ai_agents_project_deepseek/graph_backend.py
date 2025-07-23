import os
from typing import TypedDict, List
from langgraph.graph import StateGraph
#from langchain_community.chat_models import ChatDeepSeek
from langchain.chat_models import ChatOpenAI
from langchain.tools import tool
from bs4 import BeautifulSoup
import requests

# Load DeepSeek API key from environment

llm = ChatOpenAI(
    model="deepseek-chat",
    openai_api_key=os.getenv("DEEPSEEK_API_KEY"),
    openai_api_base="https://api.deepseek.com/v1",
)

@tool
def search_google(query: str) -> list:
    """Search top 20 URLs for a given query (mocked)."""
    return [f"https://example.com/article{i}" for i in range(1, 21)]

@tool
def scrape_url(url: str) -> str:
    """Scrape raw text content from a URL."""
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.get_text()
    except:
        return ""

@tool
def summarize_text(text: str) -> str:
    """Summarize a given block of text using LLM."""
    prompt = f"Summarize this content:\n{text[:3000]}"
    return llm.invoke(prompt)

@tool
def synthesize_insights(summaries: list) -> str:
    """Generate final optimized insight from multiple summaries."""
    joined = "\n\n".join(summaries)
    prompt = f"Based on the following summaries, provide an optimized response:\n{joined[:8000]}"
    return llm.invoke(prompt)

class GraphState(TypedDict):
    query: str
    links: List[str]
    pages: List[str]
    summaries: List[str]
    final_response: str

def create_graph():
    graph = StateGraph(GraphState)

    def get_links(state):
        return {"links": search_google(state["query"])}

    def scrape(state):
        return {"pages": [scrape_url(url) for url in state["links"]]}

    def summarize(state):
        return {"summaries": [summarize_text(text) for text in state["pages"]]}

    def synthesize(state):
        return {"final_response": synthesize_insights(state["summaries"])}

    graph.add_node("search", get_links)
    graph.add_node("scrape", scrape)
    graph.add_node("summarize", summarize)
    graph.add_node("synthesize", synthesize)

    graph.set_entry_point("search")
    graph.add_edge("search", "scrape")
    graph.add_edge("scrape", "summarize")
    graph.add_edge("summarize", "synthesize")
    graph.set_finish_point("synthesize")

    return graph.compile()
