import streamlit as st
from scraper import scrape_any_url
from llm_setup import initialize_llm
from graph_generation import create_knowledge_graph
from qa_chain import create_qa_chain, run_qa_chain
from save_graph import save_graph
from langchain_core.documents import Document
from langchain_experimental.graph_transformers import LLMGraphTransformer

def main():
    st.title("ASK")

    # Input URL from user
    url = st.text_input("Enter your URL:", "",key="url_input")
    
    if "scraped_data" not in st.session_state:
        st.session_state.scraped_data = None

    if st.button("Submit URL",key="unique_submit_url"):
        if url:
            with st.spinner("Scraping the content..."):
                st.session_state.scraped_data = scrape_any_url(url)
                st.success("Content scraped successfully!")
        else:
            st.error("Please enter a URL.")

    if st.session_state.scraped_data:
        with st.spinner("Initializing the LLM and generating the knowledge graph..."):
            llm = initialize_llm()
            llm_transformer = LLMGraphTransformer(llm=llm)
            docs = [Document(page_content=st.session_state.scraped_data)]
            graph_docs = llm_transformer.convert_to_graph_documents(docs)
            graph = create_knowledge_graph(graph_docs)
            save_graph(graph, url)
            st.success(f"Knowledge graph saved for {url}.")
        
        #open the chat interface
        st.header("Chat with the LLM")
        question = st.text_input("Ask a question:", "",key="question_input")

        if st.button("Ask", key="ask_question"):
            if question:
                with st.spinner("Running QA Chain..."):
                    chain = create_qa_chain(llm, graph)
                    answer = run_qa_chain(chain, question)
                st.subheader("Answer:")
                st.write(answer)
            else:
                st.error("Please enter a question.")




if __name__ == "__main__":
    main()
