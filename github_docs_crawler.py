import os
import json
import requests
from pathlib import Path
import time

def get_api_urls_from_knowledge_file(knowledge_file_path_str: str) -> list[str]:
    """Reads API URLs from a .knowledge file.

    Args:
        knowledge_file_path_str: The path to the .knowledge file.

    Returns:
        A list of API URLs. Returns an empty list if the file is not found,
        cannot be read, or contains no valid URLs.
    """
    urls = []
    try:
        knowledge_file_path = Path(knowledge_file_path_str)
        if not knowledge_file_path.is_file():
            print(f"Error: Knowledge file not found: {knowledge_file_path_str}")
            return []
        
        with open(knowledge_file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                url = line.strip()
                if not url or url.startswith('#'): # Skip empty lines and comments
                    continue
                
                if not url.startswith("https://api.github.com/repos/"):
                    print(f"Warning: The URL on line {line_num} in {knowledge_file_path_str} does not look like a GitHub API contents URL: {url}")
                    # We'll still add it, but the user should be aware.
                urls.append(url)
        
        if not urls:
            print(f"Warning: No valid URLs found in {knowledge_file_path_str}")
            
        return urls
    except Exception as e:
        print(f"Error reading knowledge file {knowledge_file_path_str}: {e}")
        return []

MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 5 # Initial delay, can be increased
REQUEST_TIMEOUT_SECONDS = 15 # Timeout for requests

def crawl_github_docs(api_url: str, output_file_handle, headers: dict, depth: int = 0):
    """Recursively crawls GitHub API for markdown files and appends their content.

    Args:
        api_url: The GitHub API URL for the current directory.
        output_file_handle: File handle for the output markdown file.
        headers: Headers for the API request (may include auth).
        depth: Current recursion depth (for logging/debugging).
    """
    indent = "  " * depth
    print(f"{indent}Crawling API URL ({depth=}): {api_url}")

    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(api_url, headers=headers, timeout=REQUEST_TIMEOUT_SECONDS)
            response.raise_for_status()  # Raises HTTPError for bad responses (4XX or 5XX)
            
            items = response.json()
            if not isinstance(items, list):
                # If the API URL points directly to a file, it returns a dict, not a list.
                # We should ideally handle this if a .knowledge file could point to a single .md file API URL.
                # For now, assuming .knowledge points to a directory listing API URL.
                if isinstance(items, dict) and items.get('type') == 'file' and items.get('name', '').endswith('.md'):
                    # This means the initial api_url was for a single file.
                    items = [items] # Treat as a list with one item
                else:
                    print(f"{indent}Error: Expected a list of items from API, but got {type(items)}. URL: {api_url}")
                    return

            # Small delay to be polite to the API, especially if unauthenticated
            time.sleep(0.5 if headers.get("Authorization") else 1.5) 

            for item in items:
                item_name = item.get('name', '[Unknown Name]')
                item_type = item.get('type', '[Unknown Type]')
                item_path = item.get('path', '[Unknown Path]') # Full path in repo

                if item_type == 'file' and item_name.endswith('.md'):
                    print(f"{indent}  - Found Markdown file: {item_path}")
                    download_url = item.get('download_url')
                    if not download_url:
                        print(f"{indent}    Warning: No download_url found for file: {item_path}")
                        continue
                    
                    try:
                        file_content_response = requests.get(download_url, headers=headers, timeout=REQUEST_TIMEOUT_SECONDS)
                        file_content_response.raise_for_status()
                        markdown_content = file_content_response.text
                        
                        output_file_handle.write(f"\n\n---\n\n<!-- Source: {item_path} -->\n\n---\n\n")
                        output_file_handle.write(markdown_content)
                        output_file_handle.flush() # Ensure content is written immediately
                        print(f"{indent}    Successfully processed and appended: {item_path}")
                        time.sleep(0.2) # Small delay after successful file download
                    except requests.exceptions.RequestException as e_file:
                        print(f"{indent}    Error downloading file {item_path} from {download_url}: {e_file}")
                    except IOError as e_io:
                        print(f"{indent}    Error writing file content for {item_path} to output: {e_io}")

                elif item_type == 'dir':
                    print(f"{indent}  - Found directory: {item_path}. Descending...")
                    dir_api_url = item.get('url')
                    if not dir_api_url:
                        print(f"{indent}    Warning: No API URL found for directory: {item_path}")
                        continue
                    crawl_github_docs(dir_api_url, output_file_handle, headers, depth + 1)
            
            return # Success, exit retry loop

        except requests.exceptions.HTTPError as e_http:
            if e_http.response.status_code == 403 and 'rate limit exceeded' in e_http.response.text.lower():
                print(f"{indent}Rate limit exceeded for {api_url}. Check GITHUB_TOKEN or wait. Attempt {attempt + 1}/{MAX_RETRIES}")
                if "Retry-After" in e_http.response.headers:
                    retry_after = int(e_http.response.headers["Retry-After"])
                    print(f"{indent}GitHub suggests waiting {retry_after} seconds.")
                    time.sleep(retry_after + 1) # Add a small buffer
                else:
                    time.sleep(RETRY_DELAY_SECONDS * (attempt + 1)) # Exponential backoff
            elif e_http.response.status_code == 404:
                 print(f"{indent}Error 404: Not Found for API URL: {api_url}. This might mean the path in your .knowledge file is incorrect or the resource is private and requires a token with permissions. Attempt {attempt + 1}/{MAX_RETRIES}")
                 # For 404, retrying might not help if the URL is fundamentally wrong.
                 if attempt < MAX_RETRIES -1:
                     time.sleep(RETRY_DELAY_SECONDS)
                 else:
                     print(f"{indent}Giving up on {api_url} after {MAX_RETRIES} attempts for 404 error.")
                     return # Give up on this URL after max retries for 404
            else:
                print(f"{indent}HTTP error for {api_url}: {e_http}. Attempt {attempt + 1}/{MAX_RETRIES}")
                if attempt < MAX_RETRIES -1:
                    time.sleep(RETRY_DELAY_SECONDS * (attempt + 1))
                else:
                    print(f"{indent}Giving up on {api_url} after {MAX_RETRIES} attempts.")
                    return # Give up on this URL
        except requests.exceptions.RequestException as e_req:
            print(f"{indent}Request error for {api_url}: {e_req}. Attempt {attempt + 1}/{MAX_RETRIES}")
            if attempt < MAX_RETRIES -1:
                time.sleep(RETRY_DELAY_SECONDS * (attempt + 1))
            else:
                print(f"{indent}Giving up on {api_url} after {MAX_RETRIES} request error attempts.")
                return # Give up on this URL
        except json.JSONDecodeError as e_json:
            print(f"{indent}Error decoding JSON from API response for {api_url}: {e_json}. Content: {response.text[:200]}...")
            return # Cannot proceed if JSON is invalid
        except Exception as e_gen:
            print(f"{indent}An unexpected error occurred while processing {api_url}: {e_gen}. Attempt {attempt + 1}/{MAX_RETRIES}")
            if attempt < MAX_RETRIES -1:
                time.sleep(RETRY_DELAY_SECONDS * (attempt + 1))
            else:
                print(f"{indent}Giving up on {api_url} after {MAX_RETRIES} unexpected error attempts.")
                return # Give up on this URL

def main():
    """
    Main function to orchestrate the documentation crawling process.
    """
    KNOWLEDGE_FILES = [
        # "nuxtjs/.knowledge", 
        # "ionicframework/.knowledge",
        # "laravel/.knowledge",
        # "filamentphp/.knowledge",
        # "livewire/.knowledge",
        "editorjs/.knowledge"
    ]  # TODO: Make this dynamic or configurable
    GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

    print("Starting documentation crawler...")

    if not GITHUB_TOKEN:
        print("\n--------------------------------------------------------------------------------")
        print("Warning: GITHUB_TOKEN environment variable not set.")
        print("You will likely encounter GitHub API rate limits without a token.")
        print("Please create a Personal Access Token (PAT) with 'repo' or 'public_repo' scope.")
        print(f'Set it as an environment variable: export GITHUB_TOKEN="YOUR_TOKEN_HERE"')
        print("More info: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens")
        print("--------------------------------------------------------------------------------\n")
        # For now, we'll proceed, but crawling might fail quickly.

    headers = {"Accept": "application/vnd.github.v3+json"} # Recommended by GitHub API docs
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    headers["User-Agent"] = "MyDocsCrawler/1.0 (Python Script)" # Good practice to set a User-Agent

    for knowledge_file_path_str in KNOWLEDGE_FILES:
        print(f"\nProcessing knowledge file: {knowledge_file_path_str}")
        start_api_urls = get_api_urls_from_knowledge_file(knowledge_file_path_str)

        if not start_api_urls:
            print(f"Skipping {knowledge_file_path_str} due to no valid URLs found or error reading file.")
            continue

        # Derive doc_name from the parent directory of the .knowledge file
        doc_name = Path(knowledge_file_path_str).parent.name
        if not doc_name: # Should not happen if path is like 'folder/.knowledge'
            doc_name = Path(knowledge_file_path_str).stem # Fallback if .knowledge is in root
        
        output_dir = Path(doc_name)
        try:
            output_dir.mkdir(parents=True, exist_ok=True)
            print(f"Output directory: {output_dir.resolve()}")
        except Exception as e:
            print(f"Error creating output directory {output_dir}: {e}")
            continue
            
        output_md_path = output_dir / "docs.md"

        print(f"Processing documentation for: '{doc_name}'")
        print(f"Found {len(start_api_urls)} GitHub API URL(s):")
        for i, url in enumerate(start_api_urls):
            print(f"  [{i+1}] {url}")
        print(f"Output will be saved to: {output_md_path.resolve()}")

        try:
            with open(output_md_path, 'w', encoding='utf-8') as output_file_handle:
                output_file_handle.write(f"# Combined Documentation for {doc_name}\n")
                output_file_handle.write(f"<!-- Source .knowledge file: {knowledge_file_path_str} -->\n")
                output_file_handle.write(f"<!-- GitHub API Roots: {', '.join(start_api_urls)} -->\n\n")
                for start_api_url in start_api_urls:
                    print(f"\n--- Starting crawl for API URL: {start_api_url} ---")
                    crawl_github_docs(start_api_url, output_file_handle, headers)
                    print(f"--- Finished crawl for API URL: {start_api_url} ---")

            print(f"Successfully processed {doc_name}. Output at {output_md_path.resolve()}")
        except IOError as e:
            print(f"Error opening or writing to output file {output_md_path}: {e}")
            continue

    # TODO: Call to helper functions and the main crawler will be added

if __name__ == "__main__":
    main()
    print("\nDocumentation crawling process initiated.") 