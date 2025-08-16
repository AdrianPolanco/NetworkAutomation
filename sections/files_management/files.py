

with open('../../files/file1.txt', 'a+') as file:
    file.write("This file1.txt was created by the files_management/files.py script.\n")
    content = file.read(5) # Read the first 5 characters
    print(content)
    content = file.read(5) # Read the next 5 characters after the previous read
    print(content)
    cursor_position = file.tell() # Get the current cursor position
    print(f"Cursor position after reading: {cursor_position}")
    file.seek(0) # Move the cursor back to the beginning of the file
    content = file.read() # Read the entire content of the file
    print("File content after writing and reading:")
    print(content)
# The file is opened in 'a+' mode, which allows reading and appending.

print(f"File operations completed successfully and file1.txt is closed: {file.closed}")
