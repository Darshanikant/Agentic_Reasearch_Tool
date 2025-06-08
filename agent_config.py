# agent_config.py
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load API Key from .env
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Setup Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GOOGLE_API_KEY)

# Example prompt template (you'll use this in summarize)
summary_prompt = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following content in bullet points:\n\n{text}"
)

# LangChain LLMChain
summarizer_chain = LLMChain(llm=llm, prompt=summary_prompt)
