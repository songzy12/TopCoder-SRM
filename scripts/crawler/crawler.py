import requests
from bs4 import BeautifulSoup
import os
import re
from pathlib import Path

# Base URL for the SRM archive
base_url = "https://archive.topcoder.com"
srm_index_url = f"{base_url}/ProblemArchive"

ROOT_DIR = Path(__file__).resolve().parents[2]
OUTPUT_DIR = ROOT_DIR / "data" / "archive"

def get_page_content(url):
    """Fetches the content of a web page."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def main():
    """Main function to crawl and save SRM content."""
    print(f"Fetching SRM index from {srm_index_url}")
    index_content = get_page_content(srm_index_url)

    if not index_content:
        print("Could not fetch the main index page. Exiting.")
        return

    soup = BeautifulSoup(index_content, 'html.parser')

    # This is a placeholder. The actual parsing logic will depend on the page structure.
    # We need to find the links to the individual SRM pages.
    # We will also try to extract the year from the surrounding HTML (like a table row).
    srm_links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if '/ProblemStatement/' in href or '/RoundOverview/' in href:
            # Construct absolute URL if it's a relative path
            if not href.startswith('http'):
                href = f"{base_url}{href}"
            
            # Find year from the "date" column or surrounding text
            year = "unknown_year"
            parent = link.parent
            for _ in range(5):  # Traverse up to 5 levels (e.g. td -> tr)
                if parent is None:
                    break
                text = parent.get_text(separator=' ')
                # Match years like 1999, 2012, 2024
                match = re.search(r'\b(199\d|20[0-2]\d)\b', text)
                if match:
                    year = match.group(1)
                    break
                parent = parent.parent

            srm_links.append((href, year))

    print(f"Found {len(srm_links)} potential SRM links.")

    # Create the main archive directory if it doesn't exist
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for srm_url, year in srm_links:
        # Extract the path from the URL to create a directory structure
        from urllib.parse import urlparse
        parsed_url = urlparse(srm_url)
        path_parts = [p for p in parsed_url.path.split('/') if p]
        
        srm_content = get_page_content(srm_url)
        if srm_content:
            # Fallback: if we didn't find the year in the index, try looking in the content
            if year == "unknown_year":
                year_match = re.search(r'\b(199\d|20[0-2]\d)\b', srm_content)
                if year_match:
                    year = year_match.group(1)

            # Store in data/archive/<year>/<path_parts>
            dir_path = OUTPUT_DIR / year / Path(*path_parts[:-1]) if len(path_parts) >= 2 else OUTPUT_DIR / year
            dir_path.mkdir(parents=True, exist_ok=True)

            # Sanitize filename
            filename = path_parts[-1] + ".html" if path_parts else "index.html"
            filepath = dir_path / filename
            filepath.write_text(srm_content, encoding='utf-8')
            print(f"Saved content from {srm_url} to {filepath}")

if __name__ == "__main__":
    main()
