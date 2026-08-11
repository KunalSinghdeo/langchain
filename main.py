from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()

def main():
    print('hello from langchain')
    information = """
    Space Exploration Technologies Corp., doing business as SpaceX, is an American spaceflight, telecommunications, and artificial intelligence company headquartered at the Starbase development site in Starbase, Texas.[7] The company operates three divisions: "Space", which conducts more orbital launches annually than any other launch provider, including national programs;[8][9] "Connectivity", which operates Starlink, a communications satellite company; and "Artificial intelligence", which operates Grok, X, and data centers.[2]

The company is credited with advances in rocket propulsion, reusable launch vehicles, human spaceflight, satellite constellation technology. The company's largest customers include NASA, the United States Space Force, and the National Reconnaissance Office. Elon Musk owns 42% of the outstanding shares of SpaceX and controls 85% of the voting power via his super-voting stock.

SpaceX was founded in 2002 by Elon Musk with the goal of reducing spaceflight costs, improving the reliability of access to outer space for ordinary humans, and colonizing Mars. In 2008, after three failed attempts between 2006 and 2008 that almost pushed the company to bankruptcy, SpaceX successfully launched the Falcon 1 into orbit, becoming the first private company to develop and launch a liquid-fueled rocket to orbit. In 2010, the company launched the Falcon 9 launch vehicle and the Dragon 1 spacecraft to fulfill NASA's Commercial Orbital Transportation Services (COTS) contracts for cargo deliveries to the International Space Station (ISS). In 2012, SpaceX began flying Commercial Resupply Services missions to the ISS, becoming the first private company to successfully dock with the station, and started developing technologies to make the Falcon 9 first stage reusable. In 2015, Falcon 9 flight 20 was the first successful landing of an orbital-class rocket's first stage and the company's SES-10 completed the first reflight of an orbital-class booster in 2017. After a decade of development, the Falcon Heavy, which consists of three Falcon 9-derived boosters, made its maiden flight in 2018. As of May 2026, Falcon 9 launches averaged approximately three missions per week, and Falcon boosters had completed nearly 650 landings and reflights.
    """

    summary_template = """
    given the information {information} about a company I want you to create:
    1. A short summary
    2. two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model = "gpt-5")
    # llm = ChatOllama(temperature=0, model = "gemma3:270m")
    chain = summary_prompt_template | llm
    response = chain.invoke(input = {"information": information})

    print(response.content)

if __name__ == "__main__":
    main()