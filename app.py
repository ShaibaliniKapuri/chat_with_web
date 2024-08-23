import streamlit as st
from scraper import scrape_any_url
from llm_setup import initialize_llm
from graph_generation import create_knowledge_graph
from qa_chain import create_qa_chain, run_qa_chain
from save_graph import save_graph
from langchain_core.documents import Document
from langchain_experimental.graph_transformers import LLMGraphTransformer

def main():
    st.title("Ask")

    # Input URL and question from user
    url = st.text_input("Enter your URL:", "")
    question = st.text_input("Enter your question:", "")
    
    if st.button("Run"):
        if url and question:
            with st.spinner("Scraping the content..."):
                scraped_data = scrape_any_url(url)
                #st.text_area("Scraped Data:", scraped_data[:1000])

            with st.spinner("Initializing the LLM..."):
                llm = initialize_llm()

            with st.spinner("Generating the Knowledge Graph..."):
                llm_transformer = LLMGraphTransformer(llm=llm)
                docs = [Document(page_content=scraped_data)]
                graph_docs = llm_transformer.convert_to_graph_documents(docs)
                graph = create_knowledge_graph(graph_docs)
                save_graph(graph, url)
                #st.success(f"Knowledge graph saved for {url}.")

            with st.spinner("Running QA Chain..."):
                chain = create_qa_chain(llm, graph)
                answer = run_qa_chain(chain, question)
                #st.success("QA Chain complete!")

            # Display the answer
            st.subheader("Answer:")
            st.write(answer)
        else:
            st.error("Please enter both a URL and a question.")

if __name__ == "__main__":
    main()
