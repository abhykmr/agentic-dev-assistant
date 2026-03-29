from langchain.agents import initialize_agent
from langchain.tools import Tool
from langchain_community.llms import Ollama


from tools.search_tools import search_docs
from tools.browser_tools import browse_website
from tools.file_tools import read_file


def create_agent():

    # llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    llm = Ollama(model="deepseek-coder")

    tools = [

        Tool(
            name="Search Docs",
            func=search_docs,
            description="Search documentation"
        ),

        Tool(
            name="Browse Website",
            func=browse_website,
            description="Open a website and read content"
        ),

        Tool(
            name="Read File",
            func=read_file,
            description="Read local files"
        )
    ]

    agent = initialize_agent(
        tools,
        llm,
        agent="zero-shot-react-description",
        verbose=True
    )

    return agent