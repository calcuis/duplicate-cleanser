import os

def find_duplicates(directory):
    # Dictionary to store file hashes
    hash_dict = {}
    # List to store duplicate file paths
    duplicates = []

    # Traverse the directory
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.lower().endswith('.png'):
                filepath = os.path.join(root, filename)
                # Calculate the hash of the file
                with open(filepath, 'rb') as f:
                    file_hash = hash(f.read())
                
                # Check if the hash already exists
                if file_hash in hash_dict:
                    duplicates.append(filepath)
                else:
                    hash_dict[file_hash] = filepath

    return duplicates

def delete_duplicates(duplicates):
    # Delete duplicate files
    for duplicate in duplicates:
        os.remove(duplicate)
        print(f"Deleted duplicate file: {duplicate}")

if __name__ == "__main__":
    current_directory = os.getcwd()
    duplicates = find_duplicates(current_directory)

    if duplicates:
        print("Duplicate files found:")
        for duplicate in duplicates:
            print(duplicate)
        
        delete_duplicates(duplicates)
        print("Duplicate files deleted.")
    else:
        print("No duplicate files found.")
