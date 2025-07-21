def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print(f"Contents of '{filename}':\n")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")


file_name = 'Sample.txt'


read_file(file_name)
