from agents import build_reader_agent,  writer_chain, critic_chain, llm
from tools import web_search, scrape_url, scholar_search
import re
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
def run_research_pipeline(topic : str) -> dict:
    state={}

    print("\n"+ " ="*50)
    print("step 1 - search agent is working...")
    print("\n"+ " ="*50)
    deep_research = False
    if deep_research:

        tavily_results = web_search.invoke({
            "query": topic + " latest 2025 2026"
        })

        scholar_results = scholar_search.invoke({
            "query": topic
        })

        state["search_results"] = f"""
    WEB RESULTS
    ===========

    {tavily_results}

    ACADEMIC RESULTS
    ================

    {scholar_results}
    """

    else:

        state["search_results"] = web_search.invoke({
            "query": topic + " latest 2025 2026"
        })   

    
    print("\n search result",state['search_results'])

    print("\n"+" ="*50)



    print("step 2 - Reader agent is scraping top resources ...")
    print("="*50)

    urls = re.findall(r'https?://\S+', state["search_results"])
    urls = list(set(urls)) 
    top_urls = urls[:9]  
    print("\n Top URLs:", top_urls)
    combined_content = ""

    for url in top_urls:
        print(f"\n Scraping: {url}")
        content = scrape_url.invoke({"url": url})
        combined_content += content + "\n\n"

    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke({
        "messages": [("user",
            f"Clean and organize the following research content about the RESEARCH TOPIC: '{topic}', "
            f"pick the most relevant URL and scrape it for deeper content and extract the most important insights.\n\n"
            f"Web Search Results:\n{state['search_results']}"
            f"Scraped Content: {combined_content}"

            """Extract:
        1. Key findings
        2. Important statistics
        3. Recent developments (focus on 2024–2026)
        4. Important and relevant sources
        5. Contradictory findings if any
        

        Return clean, structured notes.

        Be detailed."""

        )]
    })

    state['scraped_content'] = reader_result['messages'][-1].content

    print("\nscraped content: \n", state['scraped_content'])

    print("\n"+" ="*50)
    print("step 3 - Writer is drafting the report...")
    print("="*50)

    research_combined=(
        f"SEARCH RESULTS : \n {state['search_results']} \n\n"
        f"DETAILED SCRAPED CONTENT : \n {state['scraped_content']}"
    )


    print("\n"+" ="*50)
    print("step 3 - Writer is drafting the report...")
    print("="*50)


    classifier = llm.invoke(f"""
    Classify the topic into ONE word:
    - person
    - research

    Topic: {topic}

    Return ONLY one word.
    """)

    topic_type = classifier.content.strip().lower()
    print("\n Detected topic type:", topic_type)



    if topic_type == "person":

        dynamic_prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an expert biography writer."),
            ("human", """
    Write a detailed profile.

    Topic: {topic}

    Research:
    {research}

    Structure:
    - Introduction
    - Background / Early Life
    - Career / Major Work
    - Achievements
    - Recent News / Updates
    - Public Image / Influence
    - Conclusion
    - Sources

    Rules:
    - Use ONLY provided data
    - Do NOT hallucinate
    """)
        ])

    else:

        dynamic_prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an expert research writer."),
            ("human", """
    Write a detailed research report.

    Topic: {topic}

    Research:
    {research}

    Structure:
    - Executive Summary
    - Introduction
    - Background
    - Current State
    - Key Findings
    - Recent Developments
    - Statistics
    - Challenges
    - Future Outlook
    - Conclusion
    - Sources

    Rules:
    - Use ONLY provided data
    - Do NOT hallucinate
    """)
        ])


    dynamic_writer = dynamic_prompt | llm | StrOutputParser()


    state["report"] = dynamic_writer.invoke({
        "topic": topic,
        "research": research_combined
    })

    print("\n Final Report\n", state['report'])

    print("\n"+" ="*50)
    print("step 4 - critic is reviewing the report ")
    print("="*50)

    state["feedback"]=critic_chain.invoke({
        "report":state['report']
    })

    print("\n critic report \n", state['feedback'])

    return state

if __name__ == "__main__":
    topic = input("\n Enter a research topic : ")
    run_research_pipeline(topic)
