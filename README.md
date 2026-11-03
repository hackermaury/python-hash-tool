# python-hash-tool
A simple Python tool to generate MD5, SHA1, and SHA-256 hashes.


import hashlib
import os

# Available hash algorithms
ALGORITHMS = {
    "1": "md5",
    "2": "sha1",
    "3": "sha256",
    "4": "sha512"
}


def hash_text(text, algorithm):
    """Generate hash of text using hashlib."""
    data = text.encode("utf-8")
    result = hashlib.new(algorithm, data)
    return result.hexdigest()


def hash_file(file_path, algorithm):
    """Generate hash of a real file."""
    hasher = hashlib.new(algorithm)

    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(4096)

            if not chunk:
                break

            hasher.update(chunk)

    return hasher.hexdigest()


def verify_hash(original_hash, new_hash):
    """Compare two hashes."""
    return original_hash.lower() == new_hash.lower()


def main():
    print("\n===== PYTHON HASH SECURITY TOOL =====")
    print("1. MD5")
    print("2. SHA1")
    print("3. SHA256")
    print("4. SHA512")

    choice = input("\nSelect algorithm: ")

    if choice not in ALGORITHMS:
        print("Invalid algorithm!")
        return

    algorithm = ALGORITHMS[choice]

    print("\n1. Hash Text")
    print("2. Hash File")
    print("3. Verify Hash")

    action = input("\nSelect option: ")

    if action == "1":
        text = input("Enter text: ")
        result = hash_text(text, algorithm)

        print("\nAlgorithm:", algorithm.upper())
        print("Hash:", result)

    elif action == "2":
        path = input("Enter file path: ")

        if not os.path.isfile(path):
            print("File not found!")
            return

        result = hash_file(path, algorithm)

        print("\nFile:", path)
        print("Algorithm:", algorithm.upper())
        print("Hash:", result)

    elif action == "3":
        text = input("Enter original text: ")
        expected = input("Enter expected hash: ")

        actual = hash_text(text, algorithm)

        if verify_hash(expected, actual):
            print("\nHash MATCHED!")
        else:
            print("\nHash NOT MATCHED!")

        print("Calculated:", actual)

    else:
        print("Invalid option!")


if __name__ == "__main__":
    main()
