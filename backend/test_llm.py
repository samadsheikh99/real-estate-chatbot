from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    task="text-generation"
    
)

model=ChatHuggingFace(llm=llm)

template = """
You are a real estate agent. Write a description for:
Type: {property_type}, City: {city}
"""

prompt = PromptTemplate(
    input_variables=["property_type", "city"],
    template=template
)

chain = prompt | model

output = chain.invoke({
    "property_type": "Apartment",
    "city": "Islamabad"
})

print("Generated:", output)
