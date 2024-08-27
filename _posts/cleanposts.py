import os

def remove_guid_lines(file_path):
    with open(file_path, 'r', encoding='iso-8859-1') as file:
        print(file_path)
        lines = file.readlines()
    
    with open(file_path, 'w') as file:
        for line in lines:
            if not line.startswith("guid:"):
                file.write(line)

def process_files_in_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            remove_guid_lines(file_path)

if __name__ == "__main__":
    current_directory = os.getcwd()
    process_files_in_directory(current_directory)
