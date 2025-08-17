import csv

def read_csv():
    with open('../../files/airtravel.csv', 'r') as airtravel_file:
        airtravel_reader = csv.reader(airtravel_file)
        # Read the header
        header = next(airtravel_reader)
        print(header)
        print('#' * 20)
        # Read the rest of the file
        for row in airtravel_reader:
            print(row)

def write_csv():
    # Using newline='' to prevent extra blank lines in Windows
    with open('../../files/people.csv', 'a+', newline='') as people_file:
        writer = csv.writer(people_file)
        my_data = [[5, 'Daniela', 'Dublin'], [6, 'Matthew', 'Kentucky']]
        # people_file.write('\n')  # Ensure we start on a new line
        writer.writerows(my_data)
        people_file.seek(0)  # Move the cursor to the beginning of the file to read it
        content = people_file.read()
        print(content)

if __name__ == '__main__':
    write_csv()