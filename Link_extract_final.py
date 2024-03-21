import os
from bs4 import BeautifulSoup

# Function to extract hyperlinks from an HTML file
def extract_links_from_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links

# Function to save extracted links to a text file
def save_links_to_txt(links, file_path, output_folder):
    filename = os.path.basename(file_path)
    output_file_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for link in links:
            file.write(f'{link}\n')

# Function to process all HTML files in a folder
def process_html_files(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.html'):
            file_path = os.path.join(input_folder, filename)
            links = extract_links_from_html(file_path)
            save_links_to_txt(links, file_path, output_folder)
            print(f"Extracted links from {filename} and saved to {output_folder}/{os.path.splitext(filename)[0]}.txt")

# Example usage
input_folder = r'C:\Users\manda\PycharmProjects\Mandar Project\input'
output_folder = r'C:\Users\manda\PycharmProjects\Mandar Project\output'
process_html_files(input_folder, output_folder)
