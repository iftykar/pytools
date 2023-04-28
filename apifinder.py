import os
import re

# Define the directory to search
directory = '/path/to/directory'

# Define the regular expression patterns to search for API calls, URLs, and tokens
api_pattern = r'\brequests\.(get|post|put|delete)\('
url_pattern = r'https?://\S+'
token_pattern = r'(Bearer|Token)\s+\S+'

# Loop over all the files in the directory
for root, dirs, files in os.walk(directory):
    for file in files:
        # Skip non-Python files
        if not file.endswith('.py'):
            continue
        
        # Read the contents of the file
        with open(os.path.join(root, file), 'r') as f:
            contents = f.read()
        
        # Search for API calls using regular expressions
        api_matches = re.findall(api_pattern, contents)
        if api_matches:
            print(f'API calls found in {os.path.join(root, file)}:')
            for match in api_matches:
                print(f'\t{match}')
        
        # Search for URLs using regular expressions
        url_matches = re.findall(url_pattern, contents)
        if url_matches:
            print(f'URLs found in {os.path.join(root, file)}:')
            for match in url_matches:
                print(f'\t{match}')
        
        # Search for tokens using regular expressions
        token_matches = re.findall(token_pattern, contents)
        if token_matches:
            print(f'Tokens found in {os.path.join(root, file)}:')
            for match in token_matches:
                print(f'\t{match}')
