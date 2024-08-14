import os
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Walk a directory and list files with their content while applying various filters.")
    parser.add_argument("directory", help="The directory to walk")
    parser.add_argument("-skip_dir", help="Comma-separated list of directories to exclude", default="")
    parser.add_argument("-skip_file", help="Comma-separated list of files to exclude", default="")
    parser.add_argument("-output", help="The output file to save the directory structure and file contents", default="output_context.txt")
    parser.add_argument("-skip_dot", action="store_true", help="Skip all files starting with '.' except '.env'")
    parser.add_argument("-skip_css", action="store_true", help="Skip all files ending with '.css'")
    parser.add_argument("-max_size", type=int, default=1000000, help="Maximum file size in bytes to include (default: 1MB)")
    return parser.parse_args()

def should_skip_file(file, exclude_files, skip_dot, skip_css, max_size, file_path):
    if file in exclude_files:
        return True
    if skip_dot and file.startswith('.') and file != '.env':
        return True
    if skip_css and file.endswith('.css'):
        return True
    if file.endswith('.png') or file.endswith('.gif'):  # Always skip .png and .gif files
        return True
    if os.path.getsize(file_path) > max_size:
        return True
    return False

def walk_directory(directory, exclude_dirs, exclude_files, output_file, skip_dot, skip_css, max_size):
    with open(output_file, 'w', encoding='utf-8') as f:
        for root, dirs, files in os.walk(directory):
            # Filter out directories to exclude
            dirs[:] = [d for d in dirs if d not in exclude_dirs]

            # Write the directory name
            f.write(root + '\n')

            for file in files:
                file_path = os.path.join(root, file)

                # Check if we should skip this file
                if should_skip_file(file, exclude_files, skip_dot, skip_css, max_size, file_path):
                    continue

                f.write(f"{file_path}:\n")

                # Try to read and write the file content
                try:
                    with open(file_path, 'r', encoding='utf-8') as content_file:
                        content = content_file.read()
                        f.write(content)
                except Exception as e:
                    f.write(f"Error reading file: {str(e)}\n")

                f.write("\n\n")  # Add some separation between files

if __name__ == "__main__":
    args = parse_args()

    # Parse the skip_dir and skip_file arguments into sets
    exclude_dirs = set(args.skip_dir.split(",")) if args.skip_dir else set()
    exclude_files = set(args.skip_file.split(",")) if args.skip_file else set()

    # Walk the directory and write the structure and file contents to the output file
    walk_directory(args.directory, exclude_dirs, exclude_files, args.output, args.skip_dot, args.skip_css, args.max_size)
    print(f"Directory structure and file contents have been written to {args.output}")
