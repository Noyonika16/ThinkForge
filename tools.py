from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from rich import print
from tavily import TavilyClient
import os
from scholarly import scholarly
from playwright.sync_api import sync_playwright

from dotenv import load_dotenv
load_dotenv()

#client
tavily=TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query : str) -> str:
    results= tavily.search(
        query=query, 
        max_results=10, 
        search_depth="advanced",
        include_answer=False)
    out=[]
    for r in results['results']:
        out.append(
            f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n"
        )
    return "\n----\n".join(out)

@tool
def scrape_url(url : str) -> str:
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url, timeout=15000)
            page.wait_for_timeout(2500)  

            html = page.content()
            browser.close()

            soup = BeautifulSoup(html, "html.parser")

            for tag in soup(["script", "style", "nav", "footer", "header"]):
                tag.decompose()

            text = soup.get_text(separator=" ", strip=True)

            return text[:5000]

    except Exception as e:
        print(f"Playwright failed for {url}: {e}")
    try:
        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:8000]
    except Exception as e:
        return f"Could not scrape URL: {str(e)}"

@tool
def scholar_search(query: str) -> str:
    """
    Search Google Scholar and return paper titles,
    authors, year and abstracts.
    """

    try:
        search_query = scholarly.search_pubs(query)

        output = []

        for _ in range(5):
            paper = next(search_query)

            title = paper["bib"].get("title", "")
            authors = paper["bib"].get("author", "")
            year = paper["bib"].get("pub_year", "")
            abstract = paper["bib"].get("abstract", "")

            output.append(
                f"""
TITLE: {title}
AUTHORS: {authors}
YEAR: {year}
ABSTRACT: {abstract}
"""
            )

        return "\n\n".join(output)

    except Exception as e:
        return f"Scholar search failed: {str(e)}"