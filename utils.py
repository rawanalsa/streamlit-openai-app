import os
from urllib import response 
import pdfplumber
from openai import OpenAI

#create client once using env var 
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def extract_pdf_text(file):
    """Extracts text from a PDF file.""" 
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
            return text
        
def summarize_text(text):
    """Summarizes the text using OpenAI's API."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes text."},
            {"role": "user", "content": f"Summarize the following text: {text}"} #f allows variables to be inserted into the string 
        ],
        max_tokens=300, #limits the response length -> 1 token = 3/4 of a word
        temperature=0.7 #allows a more detailed/creative response 
    )
    summary = response.choices[0].message.content
    return summary 

def question_about_text(text, question):
    """Asks a question about the test using OpenAI's API."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions based on provided text."},
            {"role": "user", "content": f"Based on the following text: {text}\n\nAnswer this question: {question}"} 
        ],
        max_tokens=300,
        temperature=0.7
    )
    answer = response.choices[0].message.content
    return answer 