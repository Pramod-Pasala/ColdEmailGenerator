import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from text_preprocessor import text_preprocess

def start_app(llm, portfolio):
    
    st.title("📧 Cold Email Generator")
    url_input = st.text_input("Enter Job URL:")
    submit_button = st.button("Generate Cold Email")

    if submit_button:
        if not url_input:
            st.error("Please enter a valid URL.")
        else:
            try:
                loader = WebBaseLoader(url_input)
                data = text_preprocess(loader.load()[0].page_content)
                if "Access Denied" in data:
                    st.error("Unable to web scrape the URL.")
                    return
                portfolio.load_portfolio()
                job = llm.extract_job_info(data)
                skills = job.get("skills",[])
                links = portfolio.query_for_links(skills)
                email = llm.write_mail(job,links)
                st.write("### Generated Email:")
                st.write(email)
            except Exception as e:
                st.error(f"An error occurred. Please try with a different URL. Error: {e}")
                #st.warning("Please check the URL and try again.")

if __name__ == "__main__":
    
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    start_app(chain, portfolio)