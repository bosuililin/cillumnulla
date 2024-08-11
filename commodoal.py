import hashlib
import json

# Sample Bitwarden item dictionary
bitwarden_item = {
    "name": "Example",
    "username": "user123",
    "password": "password123",
    "url": "https://www.example.com Convert the dictionary to a JSON string
json_string = json.dumps(bitwarden_item, sort_keys=True)

# Calculate the SHA-256 hash of the JSON string
hash_object = hashlib.sha256(json_string.encode())
hash_value = hash_object.hexdigest()

print(hash_value)
