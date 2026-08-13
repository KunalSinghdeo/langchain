from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI


@tool
def search(query: str) -> str:
    '''
    Tool that searches overe internet
    Args:
        query: The query to search for
    Return:
        The Search result
    '''
    print(f"Searching for {query}")
    return "Tokyo weather is sunny"

llm = ChatOpenAI(model='gpt-5')
tools = [search]
agent = create_agent(model = llm, tools = tools) #agent is runnable


def main():
    print("Hello from langchain")
    result = agent.invoke({"messages": HumanMessage(content="What is the weather in Rourkela")})
    print(result)

if  __name__ == "__main__":
    main()