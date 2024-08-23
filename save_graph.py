import hashlib
from urllib.parse import urlparse

def save_graph(graph, url):
    # Parse the URL to extract the domain or path
    parsed_url = urlparse(url)
    
    # Create a unique identifier using a hash of the URL
    unique_identifier = hashlib.md5(url.encode()).hexdigest()
    
    # Construct the filename using the unique identifier
    filename = f"{unique_identifier}.gml"
    
    # Save the graph to a GML file
    graph.write_to_gml(filename)
    
    print(f"Graph saved as {filename}")

# Example usage:
#url = "https://huggingface.co/blog/langchain"
#save_graph(graph, url)
