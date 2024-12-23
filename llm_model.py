
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from docx import Document as docx_document  # Đảm bảo cài đặt thư viện python-docx

api_key = os.getenv("GOOGLE_API_KEY", "AIzaSyCy-F4waBhpZEwUeT5FH-ulfOT_0ySKOXw")
os.environ["GOOGLE_API_KEY"] = api_key
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

