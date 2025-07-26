from langchain.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from langchain_core.runnables import Runnable
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    task="conversational"
    
)

model=ChatHuggingFace(llm=llm)

template = """
You are a real estate agent. Write an attractive listing description based on this:

Type: {property_type}
Location: {location}, {city}
Bedrooms: {bedrooms}
Bathrooms: {baths}
Area: {area_size} {area_type}
Purpose: {purpose}

Listing:
"""

prompt = PromptTemplate(
    input_variables=["property_type", "location", "city", "bedrooms", "baths", "area_size", "area_type", "purpose"],
    template=template,
)

# ✅ Modern chain syntax
description_chain = prompt | model
