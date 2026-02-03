import os 
import streamlit as st 


from utils import extract_pdf_text, summarize_text, question_about_text

#Load environment variables from .env


def main():
    st.title("Chat GPT AI - PDF Chatbot")

    #creates an upload box
    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

    if uploaded_file is not None:
        text = extract_pdf_text(uploaded_file)
        
        #if text is not empty
        if text:
            st.write("Text extracted from the PDF:")
            st.text_area("Extracted Text", text, height=150) #displays scrollable box with the PDF text

            if st.button("Summarize Text"): #draws a button and runs the rest once its clicked once
                summary = summarize_text(text)
                st.subheader("Summary:")
                st.write(summary)

            #creates a text field 
            question = st.text_input("Ask a question based on the text")
            if st.button("Get Answer"): #this runs when user clicks the button
                if not question.strip(): #check they typed something
                    st.warning("Please type a question first. ")
                else:
                    answer = question_about_text(text, question)
                    st.subheader("Answer:")
                    st.write(answer)

        else:
            st.error("No text could be extracted from the PDF.")

if __name__ == "__main__": #only run if this file is coming from main
    main()

#many if statements because streamlit is reactive 