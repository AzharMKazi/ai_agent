# 🔍 AI Web Research Agent

This project is a multi-agent system built with **LangGraph** and **Streamlit** that:
- Accepts a user query
- Searches the web (mocked)
- Scrapes top 20 URLs
- Summarizes contents
- Synthesizes an optimized response using **DeepSeek LLM**

---

## 🧠 Agent Workflow

<pre lang="mermaid"> ```mermaid graph TD A[User Query] --> B[Search Agent (Top 20 URLs)] B --> C[Scraping Agent (Get page text)] C --> D[Summarization Agent] D --> E[Synthesis Agent] E --> F[Optimized Final Response] ``` </pre>

---

## ⚙️ Tech Stack

- [LangGraph](https://github.com/langchain-ai/langgraph) — Agent orchestration
- [LangChain](https://www.langchain.com/) — LLM tooling
- [DeepSeek LLM](https://deepseek.com/) — API-compatible language model
- [Streamlit](https://streamlit.io/) — Frontend UI
- `requests` + `BeautifulSoup` — For scraping

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
unzip ai_agents_project_deepseek.zip
cd ai_agents_project
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Set Your DeepSeek API Key

```bash
export DEEPSEEK_API_KEY=your_api_key_here  # For Linux/macOS
```

For Windows CMD:

```cmd
set DEEPSEEK_API_KEY=your_api_key_here
```

### 4. Run the App

```bash
streamlit run app.py
```

---

## ✅ Example Output

- Enter: `How does solar energy work?`
- You'll receive: synthesized insights based on top 20 URLs (mocked in this version)

---

## 🧪 To Do

- [ ] Integrate real web search (Google/Bing API)
- [ ] Use asynchronous scraping for speed
- [ ] Add persistent memory via LangChain
