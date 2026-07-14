import hashlib

def calculate_hash(file_path, algorithm="sha256"):
    """
    Calculate the hash of a file.
    Supported algorithms: md5, sha1, sha256
    """

    hash_object = hashlib.new(algorithm)

    try:
        with open(file_path, "rb") as file:
            while chunk := file.read(4096):
                hash_object.update(chunk)

        return hash_object.hexdigest()

    except FileNotFoundError:
        return "Error: File not found."
    except ValueError:
        return "Error: Unsupported hash algorithm."
    except Exception as e:
        return f"Error: {e}"


def main():
    print("===== File Hash Generator =====")

    file_path = input("Enter file path: ")

    print("\nChoose Algorithm")
    print("1. MD5")
    print("2. SHA1")
    print("3. SHA256")

    choice = input("Enter choice: ")

    algorithms = {
        "1": "md5",
        "2": "sha1",
        "3": "sha256"
    }

    algorithm = algorithms.get(choice)

    if not algorithm:
        print("Invalid choice.")
        return

    file_hash = calculate_hash(file_path, algorithm)

    print(f"\nAlgorithm : {algorithm.upper()}")
    print(f"Hash Value: {file_hash}")


if __name__ == "__main__":
    main()