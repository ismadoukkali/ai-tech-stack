from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
import json
import os
from dotenv import load_dotenv

load_dotenv()


def extract_technologies(text):
    """

    This function helps extract technologies from a job description.
    Insert the OPENAI key as 'OPENAI_API_KEY' in an .env file.

    """
    chat = ChatOpenAI(model="gpt-4-1106-preview", openai_api_key = os.getenv('OPENAI_API_KEY', 'yourapikey'))

    functions = [
        {
            "name": "extract_application_companies",
            "description": "Extract a list of the companies of applications listed on a job description",
            "parameters": {
                "type": "object",
                "properties": {
                    "applications": {
                        "type": "array",
                        "description": "List of applications listed on a job description",
                        "items": {
                            "type": "string"
                        },
                    }
                },
                "required": ["applications"],
            },
        }
    ]

    system_prompt = f"""
    You are bot that is very good at extracting tech stacks from job descriptions.
    The user will give you a job description and you should pull the names of other tools.
    The goal is to identify which applications a company is using based off their job descriptions.
    
    Example 1: "You must know Netsuite" > Netsuite
    Example 2: "We use Salesforce and Oracle" > Salesforce, Oracle

    Understand the context in which a tech stack is mentioned in a job description. For example, if the company that posted the job description is mentioning companies they work with, dont include them.
    They must be specific companies. Do not list industries or workflows or departments. Only list companies or tools that can fit in a tech stack.
    """

    output = chat(
        messages=[
            SystemMessage(content=system_prompt),
            HumanMessage(content=text),
        ],
        functions=functions,
        function_call={"name": "extract_application_companies"}
    )


    tech_found = json.loads(
        output.additional_kwargs["function_call"]["arguments"]
    )['applications']

    return list(set(tech_found))

example_job_add = "https://www.linkedin.com/jobs/view/3860727546"
print("\n")
print("\nTechnologies used at company: ", extract_technologies(""" (Insert Job Description Here)"""))


