"""
from scraper import scrape_any_url
from llm_setup import initialize_llm
from graph_generation import create_knowledge_graph
from qa_chain import create_qa_chain, run_qa_chain
from save_graph import save_graph
from langchain_core.documents import Document
from langchain_experimental.graph_transformers import LLMGraphTransformer

def main():
    #Scrape the content from the URL
    url = "https://huggingface.co/blog/langchain"
    scraped_data = scrape_any_url(url)
    

    #Initialize LLM
    llm = initialize_llm()

    #LLM Transformer
    llm_transformer = LLMGraphTransformer(llm=llm)

    #Convert the scraped document to graph documents
    docs = [Document(page_content=scraped_data)]
    graph_docs = llm_transformer.convert_to_graph_documents(docs)
    

    #knowledge graph
    graph = create_knowledge_graph(graph_docs)
    save_graph(graph, url)


    #QA chain
    chain = create_qa_chain(llm, graph)

    #Run the QA chain
    question = "What is Langchain_Huggingface?"
    answer = run_qa_chain(chain, question)
    
    #answer
    print(f"Answer: {answer}")

if __name__ == "__main__":
    main()
"""