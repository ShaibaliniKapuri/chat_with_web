import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def scrape_any_url(url):
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the title of the page
    title = soup.title.string if soup.title else 'No title found'
    #print(f"Title: {title}\n")

    """
    # Extract metadata
    #print("Metadata:")
    for meta in soup.find_all('meta'):
        meta_name = meta.get('name')
        meta_content = meta.get('content')
        if meta_name and meta_content:
            print(f"{meta_name}: {meta_content}")
    #print("\n---\n")

    # Extract headings (h1, h2, h3, etc.)
    #print("Headings:")
    for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        print(f"{heading.name}: {heading.get_text().strip()}")
    #print("\n---\n")

    # Extract paragraphs
    #print("Paragraphs:")
    for paragraph in soup.find_all('p'):
        print(paragraph.get_text().strip())
    #print("\n---\n")

    # Extract lists (ul and ol)
    #print("Lists:")
    for list_tag in soup.find_all(['ul', 'ol']):
        for li in list_tag.find_all('li'):
            print(f"• {li.get_text().strip()}")
    #print("\n---\n")

    # Extract tables
    #print("Tables:")
    for table in soup.find_all('table'):
        headers = [header.get_text().strip() for header in table.find_all('th')]
        if headers:
            print(" | ".join(headers))
        for row in table.find_all('tr'):
            columns = row.find_all('td')
            if columns:
                print(" | ".join([col.get_text().strip() for col in columns]))
        print("\n---\n")

    # Extract links (anchors)
    #print("Links:")
    base_url = f"{urlparse(url).scheme}://{urlparse(url).netloc}"
    for link in soup.find_all('a', href=True):
        href = link.get('href')
        if not href.startswith('http'):
            href = base_url + href
        print(f"{link.get_text().strip()}: {href}")
    #print("\n---\n")

    # Combine all content
    all_content = f"Title: {title}\n\n"
    all_content += "Paragraphs:\n" + "\n".join([p.get_text().strip() for p in soup.find_all('p')]) + "\n\n"
    all_content += "Headings:\n" + "\n".join([f"{h.name}: {h.get_text().strip()}" for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]) + "\n\n"
    all_content += "Lists:\n" + "\n".join([f"• {li.get_text().strip()}" for list_tag in soup.find_all(['ul', 'ol']) for li in list_tag.find_all('li')]) + "\n\n"
    #all_content += "Tables:\n"
    
    for table in soup.find_all('table'):
        headers = [header.get_text().strip() for header in table.find_all('th')]
        if headers:
            all_content += " | ".join(headers) + "\n"
        for row in table.find_all('tr'):
            columns = row.find_all('td')
            if columns:
                all_content += " | ".join([col.get_text().strip() for col in columns]) + "\n"
        all_content += "\n
    

    all_content += "Links:\n"
    for link in soup.find_all('a', href=True):
        href = link.get('href')
        if not href.startswith('http'):
            href = base_url + href
        all_content += f"{link.get_text().strip()}: {href}\n"

    return all_content
    """
     # Extract paragraphs
    paragraphs = ""
    print("Paragraphs:")
    for paragraph in soup.find_all('p'):
        paragraphs += paragraph.get_text().strip() + "\n"
        print(paragraph.get_text().strip())
    print("\n---\n")

    return paragraphs

# Example usage
#url = "https://huggingface.co/blog/langchain"
#test_doc = scrape_any_url(url)
#print(test_doc)


