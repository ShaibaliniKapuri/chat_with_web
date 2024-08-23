from langchain_community.graphs.networkx_graph import NetworkxEntityGraph

def create_knowledge_graph(graph_docs) -> NetworkxEntityGraph:
    graph = NetworkxEntityGraph()

    # Add nodes and edges to the graph
    for node in graph_docs[0].nodes:
        graph.add_node(node.id)

    for edge in graph_docs[0].relationships:
        graph._graph.add_edge(
            edge.source.id,
            edge.target.id,
            relation=edge.type,
        )

    return graph
