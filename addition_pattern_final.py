import os
import re

def replace_underscores(html_content):
    # Define the regex pattern to match href attributes containing underscores
    regex_pattern = r'(<a\s+[^>]*href=")([^"]+)"([^>]*>)'

    # Define a function to perform the replacement
    def replace_underscore(match):
        href_prefix = match.group(1)
        url = match.group(2)
        url_with_plus = url.replace('_', '+')  # Replace all underscores with plus signs in the URL
        href_suffix = match.group(3)
        return href_prefix + url_with_plus + href_suffix

    # Use regex to perform the replacement
    updated_html = re.sub(regex_pattern, replace_underscore, html_content)
    return updated_html

def process_html_file(input_file_path, output_folder):
    # Read HTML content from input file
    with open(input_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Perform replacement
    updated_html = replace_underscores(html_content)

    # Write updated HTML content to new file
    output_file_path = os.path.join(output_folder, os.path.basename(input_file_path))
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(updated_html)
    print("Updated HTML content has been saved to:", output_file_path)

def main(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each HTML file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.html'):
            input_file_path = os.path.join(input_folder, filename)
            process_html_file(input_file_path, output_folder)

if __name__ == "__main__":
    input_folder = r'C:\Users\manda\PycharmProjects\Mandar Project\input'  # Path to the folder containing input HTML files
    output_folder = r'C:\Users\manda\PycharmProjects\Mandar Project\output'  # Path to the folder where modified HTML files will be saved
    main(input_folder, output_folder)
