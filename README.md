
# Chat with Web

## Overview

"Chat with Web" is a Streamlit-based application that allows users to scrape content from a URL, generate a knowledge graph using a large language model (LLM), and interact with the LLM through a chat interface to ask questions about the content. The project integrates various components like web scraping, LLM initialization, knowledge graph generation, and question-answering (QA) chains.

## Features

- **URL Content Scraping**: Scrape and process content from any given URL.
- **LLM Integration**: Leverage LLMs (like Llama 3.1) for generating knowledge graphs and answering questions.
- **Knowledge Graph Generation**: Automatically generate a knowledge graph from the scraped content.
- **Interactive Chat Interface**: Ask questions about the scraped content in a chat interface.

## Installation

### Prerequisites

- Python 3.8+
- [Streamlit](https://streamlit.io)
- [Groq API Key](https://groq.com) (required for LLM integration)

### Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/ShaibaliniKapuri/chat_with_web.git
    cd chat_with_web
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv myenv
    source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the Groq API key:**

    Add your Groq API key to your environment variables or set it in your `.env` file:

    ```bash
    export GROQ_API_KEY=<your-api-key-here>
    ```

    Or in the `.env` file:

    ```env
    GROQ_API_KEY=<your-api-key-here>
    ```

## Usage

1. **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

2. **Use the application:**
    - First, input the URL you want to scrape.
    - Once the URL is processed, interact with the LLM by asking questions about the content through the chat interface.

## Project Structure

- `app.py`: Main Streamlit application file.
- `scraper.py`: Contains functions for scraping content from URLs.
- `llm_setup.py`: Initializes the LLM with the Groq API key.
- `graph_generation.py`: Converts documents to knowledge graph nodes and edges.
- `qa_chain.py`: Manages the question-answering chain.
- `save_graph.py`: Saves the generated knowledge graph with a unique identifier.

## Troubleshooting

- **Authentication Errors**: Ensure your Groq API key is correctly set in the environment.
- **Streamlit Widget Errors**: If you encounter duplicate widget ID errors, ensure each widget has a unique `key` argument.

## Contributing

Feel free to contribute by creating issues or submitting pull requests. Please follow the standard guidelines for contributions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to the contributors and the open-source community for their invaluable support.

