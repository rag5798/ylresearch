def read_file_to_string(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
    return file_content

file_path = 'lab.csv'  # Replace 'your_file.txt' with the path to your text file
file_content = read_file_to_string(file_path)
print(file_content)
file_content.replace('\n', '')
file_list = file_content.strip().split(",")
print(file_list)
