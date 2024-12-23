import os

# Specify the directory containing your files
directory = r'C:\Users\SHRUTI IT\OneDrive\Documents\python'

# List all .py files in the directory
files = [f for f in os.listdir(directory) if f.endswith('.py')]

# Open a file to write the combined content
with open('combined_script.py', 'w') as outfile:
    for file in files:
        file_path = os.path.join(directory, file)
        with open(file_path, 'r') as infile:
            outfile.write(f'# Content of {file}\n')  # Optional: Add file name as a comment
            outfile.write(infile.read())  # Write the content of the file
            outfile.write('\n\n')  # Add some spacing between files