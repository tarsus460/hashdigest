import hashlib

def generate_hash(file_path):
    # Open the file in binary mode to read its contents
    with open(file_path, "rb") as f:
        # Read the contents of the file
        file_contents = f.read()
        # Create a hash object using SHA-256 algorithm
        hash_object = hashlib.sha256()
        # Update the hash object with the file contents
        hash_object.update(file_contents)
        # Get the hexadecimal representation of the hash digest
        hash_digest = hash_object.hexdigest()
        return hash_digest

if __name__ == "__main__":
    # Example usage:
    file_path = input("Enter the path to the file: ")
    try:
        hash_digest = generate_hash(file_path)
        print("SHA-256 hash digest:", hash_digest)
    except FileNotFoundError:
        print("File not found.")
