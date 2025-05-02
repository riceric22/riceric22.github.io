from bs4 import BeautifulSoup
import json
import time
import requests
import sys
import os # Import os for path checking

def extract_paper_details_from_profile(html_content):
    """
    Extracts paper URLs and titles from the arXiv profile page HTML.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    papers_data = []

    # Find the table with id 'owned-articles'
    owned_articles_table = soup.find('table', id='owned-articles')

    if owned_articles_table:
        # Find all rows in the table body, skipping the header row
        # There might be multiple tbody elements, get the one with actual paper rows
        tbody = owned_articles_table.find('tbody')
        if tbody:
            rows = tbody.find_all('tr')
            # Skip the header row(s) - assuming rows with 'tbhead' are headers
            data_rows = [row for row in rows if not row.find('td', class_='tbhead')]

            for row in data_rows:
                cols = row.find_all('td')
                if len(cols) > 2:
                    # The first column contains the link to the abstract page
                    url_tag = cols[0].find('a')
                    # The third column contains the title and a link
                    title_tag = cols[2].find('a')

                    if url_tag and title_tag:
                        url = url_tag['href']
                        title = title_tag.get_text(strip=True)
                        papers_data.append({'title': title, 'url': url})

    return papers_data

def get_abstract_and_authors(paper_url):
    """
    Fetches the abstract page of a paper and extracts the abstract and authors.
    """
    try:
        # Use requests to fetch the page content
        response = requests.get(paper_url)
        response.raise_for_status() # Raise an exception for bad status codes
        abstract_page_content = response.text

        soup = BeautifulSoup(abstract_page_content, 'html.parser')

        # Extract abstract
        # The abstract is usually within a blockquote with class 'abstract'
        abstract_tag = soup.find('blockquote', class_='abstract')
        abstract = abstract_tag.get_text(strip=True).replace('Abstract:', '').strip() if abstract_tag else 'N/A'

        # Extract authors
        # Authors are usually within a div with class 'authors'
        authors_tag = soup.find('div', class_='authors')
        # Extract text and clean up
        authors = authors_tag.get_text(strip=True).replace('Authors:', '').strip() if authors_tag else 'N/A'

        return authors, abstract
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {paper_url}: {e}")
        return 'N/A', 'N/A'
    except Exception as e:
        print(f"Error parsing {paper_url}: {e}")
        return 'N/A', 'N/A'

# Main script execution
if __name__ == "__main__":
    # Set a default file path
    default_filepath = "Your arXiv.org account.html"

    # Check if a command-line argument (filepath) is provided
    if len(sys.argv) > 1:
        html_filepath = sys.argv[1]
    else:
        html_filepath = default_filepath
        print(f"No file path provided. Using default: {default_filepath}")


    # Check if the provided file path exists
    if not os.path.exists(html_filepath):
        print(f"Error: File not found at {html_filepath}")
        sys.exit(1)

    # Read the HTML content from the provided file
    try:
        with open(html_filepath, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except Exception as e:
        print(f"Error reading file {html_filepath}: {e}")
        sys.exit(1)


    # Extract initial paper data from the profile page
    papers_list = extract_paper_details_from_profile(html_content)

    # Iterate through the papers and fetch abstract and authors for each
    extracted_papers_data = []
    for paper in papers_list:
        print(f"Fetching details for: {paper['title']} ({paper['url']})")
        authors, abstract = get_abstract_and_authors(paper['url'])
        extracted_papers_data.append({
            'title': paper['title'],
            'url': paper['url'],
            'authors': authors,
            'abstract': abstract
        })
        # Add a small delay to avoid overwhelming the server
        time.sleep(1)

    # Save the extracted data to a JSON file
    output_filename = "assets/files/arxiv_papers.json"
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(extracted_papers_data, f, ensure_ascii=False, indent=4)

    print(f"\nSuccessfully extracted data for {len(extracted_papers_data)} papers and saved to {output_filename}")
