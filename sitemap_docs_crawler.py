# sitemap_docs_crawler.py
import os
import requests
import xml.etree.ElementTree as ET
from pathlib import Path
import time

try:
    from markdownify import markdownify as md
    MARKDOWNIFY_AVAILABLE = True
except ImportError:
    MARKDOWNIFY_AVAILABLE = False
    # We'll print a warning in main if it's needed and not available

# --- Configuration Constants ---
REQUEST_TIMEOUT_SECONDS = 20  # Increased timeout for potentially larger pages
RETRY_DELAY_SECONDS = 10    # Initial delay for retries
MAX_RETRIES = 3
PER_REQUEST_DELAY_SECONDS = 1 # Delay between fetching individual pages
DEFAULT_USER_AGENT = "MyDocsSitemapCrawler/1.0 (Python Script; +http://example.com/botinfo)"

# --- Sitemap Parsing Logic ---
# XML Namespace, often found in sitemaps
SITEMAP_NS = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
DEFAULT_SITEMAP_NS_URI = "http://www.sitemaps.org/schemas/sitemap/0.9"

def fetch_and_parse_sitemap(sitemap_url: str, headers: dict, visited_sitemaps: set = None) -> list[str]:
    """Fetches and parses a sitemap.xml file, handling sitemap indexes.

    Args:
        sitemap_url: The URL of the sitemap.xml file.
        headers: HTTP headers for the request.
        visited_sitemaps: A set of already visited sitemap URLs to prevent loops.

    Returns:
        A list of unique page URLs found in the sitemap(s).
    """
    if visited_sitemaps is None:
        visited_sitemaps = set()

    if sitemap_url in visited_sitemaps:
        print(f"Sitemap already visited, skipping to avoid loop: {sitemap_url}")
        return []
    visited_sitemaps.add(sitemap_url)

    page_urls = []
    print(f"Fetching sitemap: {sitemap_url}")

    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(sitemap_url, headers=headers, timeout=REQUEST_TIMEOUT_SECONDS)
            response.raise_for_status()
            sitemap_content = response.content # Use .content for ET.fromstring with bytes

            try:
                root = ET.fromstring(sitemap_content)
            except ET.ParseError as e_parse:
                print(f"Error parsing XML for {sitemap_url}: {e_parse}. Content: {sitemap_content[:500]}")
                # If direct parsing fails, we might try the stripping approach as a last resort,
                # but for now, let's focus on correct namespace handling.
                # If parsing fails outright, it's hard to proceed.
                return []

            # Check if it's a sitemap index
            # Try with default namespace URI, then with 'sm' prefix, then without any namespace
            sitemap_tag_name_variants = [
                f'{{{DEFAULT_SITEMAP_NS_URI}}}sitemap', # For default namespace
                'sm:sitemap',                           # For 'sm' prefixed namespace
                'sitemap'                               # For no namespace / stripped
            ]
            loc_tag_name_variants = [
                f'{{{DEFAULT_SITEMAP_NS_URI}}}loc',
                'sm:loc',
                'loc'
            ]

            sitemapindex_tags = []
            for variant in sitemap_tag_name_variants:
                sitemapindex_tags = root.findall(variant, SITEMAP_NS if ':' in variant else None)
                if sitemapindex_tags:
                    break
            
            if sitemapindex_tags: # It's a sitemap index
                print(f"Sitemap index found at {sitemap_url}. Processing sub-sitemaps...")
                for sitemap_tag in sitemapindex_tags:
                    loc_tag = None
                    for loc_variant in loc_tag_name_variants:
                        loc_tag = sitemap_tag.find(loc_variant, SITEMAP_NS if ':' in loc_variant else None)
                        if loc_tag is not None:
                            break
                    
                    if loc_tag is not None and loc_tag.text:
                        nested_sitemap_url = loc_tag.text.strip()
                        page_urls.extend(fetch_and_parse_sitemap(nested_sitemap_url, headers, visited_sitemaps))
            else: # It's a regular sitemap with URLs
                url_tag_name_variants = [
                    f'{{{DEFAULT_SITEMAP_NS_URI}}}url',
                    'sm:url',
                    'url'
                ]
                url_tags = []
                for variant in url_tag_name_variants:
                    url_tags = root.findall(variant, SITEMAP_NS if ':' in variant else None)
                    if url_tags:
                        break
                
                for url_tag in url_tags:
                    loc_tag = None
                    for loc_variant in loc_tag_name_variants:
                        loc_tag = url_tag.find(loc_variant, SITEMAP_NS if ':' in loc_variant else None)
                        if loc_tag is not None:
                            break

                    if loc_tag is not None and loc_tag.text:
                        page_urls.append(loc_tag.text.strip())
            
            return list(set(page_urls)) # Return unique URLs

        except requests.exceptions.HTTPError as e_http:
            print(f"HTTP error fetching sitemap {sitemap_url}: {e_http}. Attempt {attempt + 1}/{MAX_RETRIES}")
            if e_http.response.status_code == 404:
                print(f"Sitemap {sitemap_url} not found (404). Giving up.")
                return [] # No point retrying 404 for sitemap URL
            if attempt == MAX_RETRIES - 1:
                print(f"Failed to fetch sitemap {sitemap_url} after {MAX_RETRIES} attempts.")
                return []
            time.sleep(RETRY_DELAY_SECONDS * (attempt + 1))
        except requests.exceptions.RequestException as e_req:
            print(f"Request error fetching sitemap {sitemap_url}: {e_req}. Attempt {attempt + 1}/{MAX_RETRIES}")
            if attempt == MAX_RETRIES - 1:
                print(f"Failed to fetch sitemap {sitemap_url} after {MAX_RETRIES} attempts due to request error.")
                return []
            time.sleep(RETRY_DELAY_SECONDS * (attempt + 1))
        except Exception as e_gen:
            print(f"An unexpected error occurred while processing sitemap {sitemap_url}: {e_gen}. Attempt {attempt + 1}/{MAX_RETRIES}")
            if attempt == MAX_RETRIES - 1:
                print(f"Failed to process sitemap {sitemap_url} after {MAX_RETRIES} attempts due to unexpected error.")
                return []
            time.sleep(RETRY_DELAY_SECONDS * (attempt + 1))
    return [] # Should be unreachable if MAX_RETRIES > 0, but as a fallback

# --- HTML Processing Logic ---
def fetch_page_html(page_url: str, headers: dict) -> str | None:
    """Fetches the HTML content of a given page URL.

    Args:
        page_url: The URL of the page to fetch.
        headers: HTTP headers for the request.

    Returns:
        The HTML content as a string, or None if an error occurs.
    """
    print(f"  Fetching HTML page: {page_url}")
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(page_url, headers=headers, timeout=REQUEST_TIMEOUT_SECONDS)
            response.raise_for_status()
            
            content_type = response.headers.get("Content-Type", "").lower()
            if "html" not in content_type:
                print(f"    Warning: Content-Type for {page_url} is not HTML ({content_type}). Skipping.")
                return None
            
            return response.text
        except requests.exceptions.HTTPError as e_http:
            print(f"    HTTP error fetching page {page_url}: {e_http}. Attempt {attempt + 1}/{MAX_RETRIES}")
            if e_http.response.status_code == 404:
                print(f"    Page {page_url} not found (404). Giving up.")
                return None # No point retrying 404
            if attempt == MAX_RETRIES - 1:
                print(f"    Failed to fetch page {page_url} after {MAX_RETRIES} attempts.")
                return None
            time.sleep(RETRY_DELAY_SECONDS * (attempt + 1))
        except requests.exceptions.RequestException as e_req:
            print(f"    Request error fetching page {page_url}: {e_req}. Attempt {attempt + 1}/{MAX_RETRIES}")
            if attempt == MAX_RETRIES - 1:
                print(f"    Failed to fetch page {page_url} after {MAX_RETRIES} attempts due to request error.")
                return None
            time.sleep(RETRY_DELAY_SECONDS * (attempt + 1))
        except Exception as e_gen:
            print(f"    An unexpected error occurred while fetching page {page_url}: {e_gen}. Attempt {attempt + 1}/{MAX_RETRIES}")
            if attempt == MAX_RETRIES - 1:
                print(f"    Failed to fetch page {page_url} after {MAX_RETRIES} attempts due to unexpected error.")
                return None
            time.sleep(RETRY_DELAY_SECONDS * (attempt + 1))
    return None

def convert_html_to_markdown(html_content: str, page_url: str) -> str | None:
    """Converts HTML content to Markdown using markdownify.

    Args:
        html_content: The HTML content string.
        page_url: The source URL (for logging).

    Returns:
        The Markdown content as a string, or None if conversion fails.
    """
    if not MARKDOWNIFY_AVAILABLE:
        # This check is also in main, but good for safety if called directly
        print("Error: markdownify library is not available for HTML to Markdown conversion.")
        return None
    try:
        # You can customize markdownify options here if needed, e.g.:
        # md_content = md(html_content, strip=['nav', 'footer'], heading_style='atx')
        md_content = md(html_content)
        print(f"    Successfully converted HTML from {page_url} to Markdown.")
        return md_content
    except Exception as e:
        print(f"    Error converting HTML from {page_url} to Markdown: {e}")
        return None

def get_sitemap_url_from_knowledge_file(knowledge_file_path_str: str) -> str | None:
    """Reads the sitemap URL from the first line of a .knowledge file.

    Args:
        knowledge_file_path_str: The path to the .knowledge file.

    Returns:
        The sitemap URL as a string, or None if an error occurs.
    """
    try:
        knowledge_file_path = Path(knowledge_file_path_str)
        if not knowledge_file_path.is_file():
            print(f"Error: Knowledge file not found: {knowledge_file_path_str}")
            return None
        
        with open(knowledge_file_path, 'r', encoding='utf-8') as f:
            url = f.readline().strip()
        
        if not url:
            print(f"Error: Knowledge file is empty or first line is blank: {knowledge_file_path_str}")
            return None
        # Basic check for a URL, can be made more sophisticated
        if not (url.startswith("http://") or url.startswith("https://")):
            print(f"Warning: The URL in {knowledge_file_path_str} does not look like a valid HTTP/S URL: {url}")
            # We'll still return it, but the user should be aware.

        return url
    except Exception as e:
        print(f"Error reading knowledge file {knowledge_file_path_str}: {e}")
        return None

def main():
    """
    Main function to orchestrate the sitemap-based documentation crawling process.
    """
    if not MARKDOWNIFY_AVAILABLE:
        print("Error: The 'markdownify' library is not installed. ")
        print("Please install it by running: pip install markdownify")
        print("Exiting script.")
        return

    KNOWLEDGE_FILES = [
        "flutter/.knowledge",
        # Add other sitemap-based .knowledge files here, e.g.:
        # "some_other_docs/.knowledge"
    ]

    print("Starting sitemap-based documentation crawler...")

    headers = {
        "User-Agent": DEFAULT_USER_AGENT
    }

    for knowledge_file_path_str in KNOWLEDGE_FILES:
        print(f"\nProcessing knowledge file: {knowledge_file_path_str}")
        sitemap_start_url = get_sitemap_url_from_knowledge_file(knowledge_file_path_str)

        if not sitemap_start_url:
            print(f"Skipping {knowledge_file_path_str} due to missing or invalid sitemap URL.")
            continue

        doc_name = Path(knowledge_file_path_str).parent.name
        if not doc_name:
            doc_name = Path(knowledge_file_path_str).stem
        
        output_dir = Path(doc_name)
        try:
            output_dir.mkdir(parents=True, exist_ok=True)
            print(f"Output directory: {output_dir.resolve()}")
        except Exception as e:
            print(f"Error creating output directory {output_dir}: {e}. Skipping {doc_name}.")
            continue
            
        output_md_path = output_dir / "docs.md"

        print(f"Processing documentation for: '{doc_name}'")
        print(f"Sitemap URL: {sitemap_start_url}")
        print(f"Output will be saved to: {output_md_path.resolve()}")

        all_page_urls = fetch_and_parse_sitemap(sitemap_start_url, headers)

        if not all_page_urls:
            print(f"No page URLs found or sitemap processing failed for {doc_name}. Skipping.")
            continue
        
        print(f"Found {len(all_page_urls)} unique page URLs in sitemap for {doc_name}.")

        try:
            with open(output_md_path, 'w', encoding='utf-8') as output_file_handle:
                output_file_handle.write(f"# Combined Documentation for {doc_name} (from Sitemap)\n")
                output_file_handle.write(f"<!-- Source .knowledge file: {knowledge_file_path_str} -->\n")
                output_file_handle.write(f"<!-- Source Sitemap URL: {sitemap_start_url} -->\n\n")
                
                processed_count = 0
                for i, page_url in enumerate(all_page_urls):
                    print(f"\nProcessing URL {i+1}/{len(all_page_urls)}: {page_url}")
                    html_content = fetch_page_html(page_url, headers)
                    
                    if html_content:
                        markdown_content = convert_html_to_markdown(html_content, page_url)
                        if markdown_content:
                            try:
                                output_file_handle.write(f"\n\n---\n\n<!-- Source URL: {page_url} -->\n\n---\n\n")
                                output_file_handle.write(markdown_content)
                                output_file_handle.flush() # Write to disk periodically
                                processed_count += 1
                            except IOError as e_io:
                                print(f"    Error writing Markdown for {page_url} to file: {e_io}")
                        else:
                            print(f"    Skipping {page_url} due to HTML to Markdown conversion failure.")
                    else:
                        print(f"    Skipping {page_url} due to HTML fetch failure.")
                    
                    # Be polite to the server
                    if i < len(all_page_urls) - 1: # Don't sleep after the last item
                        print(f"  Waiting for {PER_REQUEST_DELAY_SECONDS}s before next request...")
                        time.sleep(PER_REQUEST_DELAY_SECONDS)

                print(f"\nSuccessfully processed {processed_count}/{len(all_page_urls)} pages for {doc_name}.")
                print(f"Output for {doc_name} saved to: {output_md_path.resolve()}")

        except IOError as e:
            print(f"Error opening or writing to output file {output_md_path}: {e}")
            continue # To the next knowledge file

    print("\nSitemap documentation crawling process finished.")

if __name__ == "__main__":
    main() 