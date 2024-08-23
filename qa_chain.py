from langchain.chains import GraphQAChain
from langchain_community.graphs.networkx_graph import NetworkxEntityGraph

def create_qa_chain(llm, graph: NetworkxEntityGraph, verbose: bool = True) -> GraphQAChain:

    return GraphQAChain.from_llm(llm=llm, graph=graph, verbose=verbose)

def run_qa_chain(chain: GraphQAChain, question: str) -> str:

    return chain.run(question)
