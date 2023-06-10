from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
#from langchain.chains import QAGenerationChain
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
from gtts import gTTS
from io import BytesIO
from langchain.chat_models import ChatOpenAI
#from pdfgen import generate_pdf

load_dotenv()

def main():
    
    st.set_page_config(page_title="Ask your PDF")
    st.header("Ask your PDF 💬")

    # Code to upload the PDF file
    pdf=st.file_uploader("Upload your PDF",type="pdf")

    hide_streamlit_style = """
            <style>
            
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

    # Code to extract the text from PDF file
    if pdf is not None:
        pdf_reader=PdfReader(pdf)
        text =""
        for page in pdf_reader.pages:
            text+=page.extract_text()
        
        #split into chunks
        text_splitter=CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function = len
        )
        chunks = text_splitter.split_text(text)

        # Create embeddings
        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunks,embeddings)

        #show user input

        #user_question = st.text_input("Ask a question:")
        on_click=st.button("Generate Q&A")
        prompt = "I want you to act as a tutor and the professor has asked you to make 10 questions and answers respectively from the given text. Please generate 2 arrays of 10 question and 10 answers corresponding to 10 questions each, wihout numbering and separated by semicolon respectively."
        # prompt = """Please generate 10 questions in the following format:

        #          Question: [Insert question here] 

        #           Answer: [Insert answer here]
                  
                  

        #         Please make sure to base your questions and answers on the provided context"""
        if on_click:
            docs=knowledge_base.similarity_search(prompt)

            llm=ChatOpenAI()
            chain=load_qa_chain(llm,chain_type="stuff")
            with get_openai_callback() as cb:
                response =chain.run(input_documents=docs,question=prompt)
                print(cb)
                
            st.write(response)
            #generate_pdf(response,'QA.pdf')
            






if __name__ == '__main__':
    main()