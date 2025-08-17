with open('../../../files/devices.txt', 'r') as file:
    data = file.read().splitlines()
    devices = data[1:]
    devices = [device.split(':') for device in devices]
    for device in devices:
        # Strip leading and trailing whitespace from each element
        device[:] = [element.strip() for element in device]
    print(devices)

# w creates the file if it does not exist, if exists overwrites it
with open('../../../files/devices_solution.txt', 'w') as solution_file:
    # Write a single string with all the data
    # For each array of strings in devices, join the elements with a space as separator
    # and then join all these strings with a newline character, finally strip the string of spaces
    content = '\n'.join([f'{device[0]} {device[1]} {device[2]} {device[3]} {device[4]}'.strip() for device in devices])
    solution_file.write(content)