# 🧠 ThinkForge — Multi-Agent AI Research System

> Turn raw questions into deep, structured insights — powered by autonomous AI agents.

---

## 🚀 Overview

**ThinkForge** is a multi-agent AI system that transforms any research query into a **comprehensive, structured report** using:

* 🌐 Real-time web search
* 🧾 Intelligent content extraction
* ✍️ LLM-powered report generation
* 🧐 Automated critique & scoring

Instead of returning a simple answer, ThinkForge simulates a **research workflow**, combining multiple AI agents to deliver **high-quality, evidence-backed insights**.

---

## 🧩 Architecture

The system is built as a **multi-agent pipeline**:

```
User Query
   ↓
🔍 Search Agent Tool (Tavily)
   ↓
📄 Scraper (Playwright + BeautifulSoup)
   ↓
🧠 Reader Agent (extracts structured insights)
   ↓
✍️ Writer Agent (generates full report)
   ↓
🧐 Critic Agent (evaluates quality)
```

---

## ⚡ Features

* 🔎 **Real-time Web Search** (Tavily API)
* 🧠 **Multi-Agent AI Pipeline** (LangChain + OpenRouter)
* 🌐 **Dynamic Web Scraping** (Playwright for JS-heavy pages)
* 📊 **Structured Research Reports**
* 🧾 **PDF Report Generation**
* 🧪 **Deep Research Mode** (Web + Academic sources)
* 🎯 **Topic-aware writing (Research vs Person)**
* 🧑‍💻 **Modern Streamlit UI**

---

## 🖥️ Demo UI

> *(Add screenshots here — highly recommended)*

---

## ⚙️ Tech Stack

* **Frontend:** Streamlit
* **LLM Framework:** LangChain, LangGraph
* **LLM Provider:** OpenRouter (GPT-OSS-120B)
* **Search API:** Tavily
* **Scraping:** Playwright + BeautifulSoup
* **PDF Generation:** ReportLab
* **Language:** Python

---

## 📦 Installation

```bash
git clone https://github.com/Noyonika16/ThinkForge.git
cd ThinkForge
pip install -r requirements.txt
playwright install
```

---

## 🔑 Environment Setup

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🧪 Example Queries

* `LLM agents 2025`
* `CRISPR gene editing latest developments`
* `NIT Agartala placement report 2025`
* `Fusion energy breakthroughs`

---

## 🧠 Deep Research Mode

Toggle **Deep Research Mode** to:

* Combine **web + academic sources**
* Extract **more detailed insights**
* Focus on **latest developments (2024–2026)**

⚠️ Note: May be slower and include partial academic data due to **paywalls**.

---

## 📊 Output

The system generates:

* 📄 Structured research report
* 🔗 Source references
* 🧐 Critic evaluation (score + feedback)
* 📥 Downloadable report (PDF / Text)

---

## ⚠️ Limitations

* Some academic sources may be paywalled
* Scraping depends on website structure
* Real-time data availability varies by topic
* LLM responses are constrained to provided data (no hallucination policy)

---

## 🚀 Future Improvements

* ⚡ Parallel scraping for faster performance
* 📚 Better academic integration (Google Scholar, PubMed, Scopus APIs and more)
* 🌍 Deployment with scalable backend
* 📊 Visual analytics dashboards
* 🧠 Memory-based multi-query reasoning
* 📸 Multimodal input and output
* 💻 Use of better api keys from OpenAI or Mistral (paid)

---

## 👩‍💻 Author

**Noyonika Mukherjee**
B.Tech CSE — AI/ML Enthusiast

---

## ⭐ Why This Project Stands Out

* Goes beyond simple chatbots
* Implements **multi-agent architecture**
* Combines **search + scraping + reasoning**
* Focuses on **real-world research workflows**

---

## 📌 License

This project is open-source and available under the MIT License.

---

⭐ If you found this interesting, consider starring the repo!
