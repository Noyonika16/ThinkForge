from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrape_url
import os
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    model="openai/gpt-oss-120b:free",
    temperature=0
)


def build_reader_agent():
    return create_agent(
        model=llm,
        tools=[scrape_url]
    )

writer_prompt=ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports. ONLY use the provided research. Do NOT invent facts. If information is missing, explicitly say 'Not enough data available'."),
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}
     
Rules:
- Use ONLY the provided data
- If data is missing, say "Not enough data available"
- Do NOT guess numbers

Structure the report as:

- Introduction
- Background
- Current State 
- Key Findings (minimum 3 well-explained points)
- Recent Developments (2024-2026 if available)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional.
Do not halucinate"""),
])

writer_chain=writer_prompt | llm | StrOutputParser()


critic_prompt=ChatPromptTemplate([
    ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain= critic_prompt | llm | StrOutputParser()