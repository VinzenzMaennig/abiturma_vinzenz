""" This code is used to interchange date and place in all slides """

import os

# Define the directory where the Markdown files are located
directory = "/"

find = "test123456"
replace = "Winter 2023 MÃ¼nchen"

# Recursive function to process the files in a directory and its subdirectories
def process_directory(dir):
    # Iterate over the files in the directory
    for filename in os.listdir(dir):
        # Check if the file is a Markdown file
        if filename.endswith(".md"):
            # Open the file in read-only mode
            with open(os.path.join(dir, filename), "r") as file:
                # Read the file content
                content = file.read()

            # Replace the old string with the new string in the file content
            content = content.replace(find, replace)

            # Open the file in write mode
            with open(os.path.join(dir, filename), "w") as file:
                # Write the modified content to the file
                file.write(content)
        # If the file is a directory, call the function recursively
        elif os.path.isdir(os.path.join(dir, filename)):
            process_directory(os.path.join(dir, filename))

# Call the function to process the files in the top-level directory
process_directory(directory)