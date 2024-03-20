import os
import shutil
from bs4 import BeautifulSoup
import re

def replace_link(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.html'):
            input_file_path = os.path.join(input_folder, filename)
            output_file_path = os.path.join(output_folder, filename)
            modify_html(input_file_path, output_file_path)

def modify_html(input_file_path, output_file_path):
    # Read the HTML file
    with open(input_file_path, 'r') as file:
        html_content = file.read()

    # Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all <a> tags
    for link in soup.find_all('a'):
        # Get the value of href attribute
        href = link.get('href')
        if href:
            # Replace the part of the link
            new_href = re.sub(r'(https://)cld-pweb-gau01.amgen.com', r'\1confluence-dvpc.devops.amgen.com', href)
            # Update the href attribute with the new link
            link['href'] = new_href

    # Write the modified HTML to a new file
    with open(output_file_path, 'w') as file:
        file.write(str(soup))

# Example usage
input_folder = r'C:\Users\manda\PycharmProjects\Mandar Project\input'  # Path to the folder containing input HTML files
output_folder = r'C:\Users\manda\PycharmProjects\Mandar Project\output'  # Path to the folder where modified HTML files will be saved
replace_link(input_folder, output_folder)
