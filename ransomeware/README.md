# Ransomeware

Basic ransomeware that encrypts files and decrypts them when the user enters the correct pass phrase.

## Basic Algorithm

1. Encrypt

- Get all files from the `files` folder
- Generate a secret key and store it in `key.key`
- Encrypt using the secret key

2. Decrypt

- Get all files from the `files` folder
- Ask user for the passphares
- If correct 
    - Decrypt using the secret key from `key.key`
- Else
    - Print exit