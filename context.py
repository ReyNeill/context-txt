import os
import sys

def write_file_content(output_file, file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except UnicodeDecodeError:
        print(f"Skipping non-text file: {file_path}")
        return

    relative_path = os.path.relpath(file_path, start=sys.argv[1])
    output_file.write(f"{relative_path} :\n")
    output_file.write(content)
    output_file.write("\n\n")

def traverse_directory(directory, output_file):
    for root, dirs, files in os.walk(directory):
        # Modify dirs in-place to skip certain directories
        dirs[:] = [d for d in dirs if d not in {"node_modules", ".NEXT", ".next"}]
        for file in files:
            file_path = os.path.join(root, file)
            write_file_content(output_file, file_path)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 txt.py <directory>")
        sys.exit(1)
    
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        sys.exit(1)
    
    output_filename = "output.txt"
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        traverse_directory(directory, output_file)
    
    print(f"Contents written to {output_filename}")

if __name__ == "__main__":
    main()
