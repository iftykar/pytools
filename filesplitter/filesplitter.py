import os
import pathlib

# function to split a file into smaller files based on number of characters
def split_file_by_chars(file_path, max_chars):
    with open(file_path, 'r') as f:
        data = f.read()
        file_name, file_ext = os.path.splitext(file_path)
        i = 0
        while i < len(data):
            with open(f'{file_name}_{i+1}{file_ext}', 'w') as new_file:
                new_file.write(data[i:i+max_chars])
            i += max_chars

# function to split a file into smaller files based on number of lines
def split_file_by_lines(file_path, max_lines):
    with open(file_path, 'r') as f:
        file_name, file_ext = os.path.splitext(file_path)
        i = 1
        while True:
            lines = f.readlines(max_lines)
            if not lines:
                break
            with open(f'{file_name}_{i}{file_ext}', 'w') as new_file:
                new_file.writelines(lines)
            i += 1

# function to split all .py files in a directory based on number of characters
def split_files_by_chars(file_path, max_chars):
    for file_name in os.listdir(directory_path):
        if file_name.endswith('.py'):
            file_path = os.path.join(directory_path, file_name)
            split_file_by_chars(file_path, max_chars)

# function to split all .py files in a directory based on number of lines
def split_files_by_lines(directory_path, max_lines):
    for file_name in os.listdir(directory_path):
        if file_name.endswith('.py'):
            file_path = os.path.join(directory_path, file_name)
            split_file_by_lines(file_path, max_lines)

# Example usage
directory_path = '/Users/iftekarmohiuddin/Downloads/emailscript/'
max_chars = 20000
max_lines = 100

split_files_by_chars(directory_path, max_chars)
split_files_by_lines(directory_path, max_lines)
