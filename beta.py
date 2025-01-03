import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document  # Import Document
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from llm_model import llm

# Thiết lập User-Agent
USER_AGENT = "MyApp/1.0"
HEADERS = {"User-Agent": USER_AGENT}

# Step 1: Đọc văn bản từ tệp data/input.txt
file_path = "data/input.txt"
try:
    with open(file_path, "r", encoding="utf-8") as file:
        text_content = file.read()
    # Chuyển đổi nội dung thành Document
    documents = [Document(page_content=text_content)]
except Exception as e:
    print(f"Error reading file {file_path}: {e}")
    documents = []

if not documents:
    print("No documents loaded. Exiting...")
    exit()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_docs = text_splitter.split_documents(documents)

map_prompt = """
You are an expert summarizer. Summarize the following text concisely:

{text}
"""

map_template = PromptTemplate(template=map_prompt, input_variables=["text"])

chain = load_summarize_chain(llm, chain_type="map_reduce", map_prompt=map_template)

try:
    final_summary = chain.invoke({"input_documents": split_docs})
    print("Final Summary:")
    print(final_summary)
except Exception as e:
    print(f"Error during summarization: {e}")
