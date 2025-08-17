

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

with open('../../files/file1.txt', 'r') as file:
    # Read the content of the file and split it into lines
    lines = file.read().splitlines()
    print("Lines in file1.txt:")
    for line in lines:
        print(line)

# Setting the file to 'w+' mode to write and read
with open('../../files/file2.txt', 'w+') as file:
    file.write("This file2.txt was created by the files_management/files.py script.\n")
    file.seek(0)  # Move the cursor back to the beginning of the file
    content = file.read()  # Read the entire content of the file
    print("File content after writing in w+ mode:")
    print(content)




print(f"File operations completed successfully and file1.txt is closed: {file.closed}")
