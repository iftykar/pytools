Python Directory File Splitter
This Python code is designed to split all .py files in a directory into smaller files based on either the number of characters or the number of lines.

Requirements
Python 3.x

How to use

Download or clone this repository to your local machine.
Open a terminal or command prompt and navigate to the directory where the repository is located.
Modify the directory_path, max_chars, and max_lines parameters in the split_files_by_chars and split_files_by_lines functions to your desired values.
Run the following command to split all .py files in the directory based on the number of characters:
css

Copy code
python file_splitter.py --chars

This will split all .py files in the directory into smaller files based on the number of characters specified in the max_chars parameter.

Run the following command to split all .py files in the directory based on the number of lines:
css

Copy code
python file_splitter.py --lines

This will split all .py files in the directory into smaller files based on the number of lines specified in the max_lines parameter.

The program will create new files with names in the format <original_file_name>_<part_number>.py in the same directory as the original files.

Note: Make sure to provide the correct path to the directory, and also adjust the max_chars or max_lines parameters to your desired file size.

That's it! You can now split all .py files in a directory into smaller files using this Python code.