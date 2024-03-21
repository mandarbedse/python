import os
import re
from bs4 import BeautifulSoup

# Function to extract hyperlinks containing a specific string from an HTML file
def extract_links_from_html(file_path, target_regex):
    print(f"Extracting links from: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and re.search(target_regex, href):  # Check if the target string is in the href using regex
            links.append(href)
    return links

# Function to save extracted links to a text file
def save_links_to_txt(links, file_path, output_folder):
    filename = os.path.basename(file_path)
    output_file_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for link in links:
            file.write(f'{link}\n')
    print(f"Saved links to: {output_file_path}")

# Function to process HTML files under a folder starting with a specific prefix
def process_html_files(input_folder, output_folder, target_regex):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                links = extract_links_from_html(file_path, target_regex)
                if links:
                    save_links_to_txt(links, file_path, output_folder)
                    print(f"Extracted links from {file_path} and saved to {output_folder}/{os.path.splitext(file)[0]}.txt")
                else:
                    print(f"No links extracted from {file_path}")

# Example usage
input_folder = r'C:\Users\manda\PycharmProjects\Mandar Project\input'
output_folder = r'C:\Users\manda\PycharmProjects\Mandar Project\output'
target_regex = r'confluence-dvpc\.devops\.amgen\.com'  # Regex pattern to match the target string in URLs

print("Processing HTML files...")
process_html_files(input_folder, output_folder, target_regex)
print("Done!")
