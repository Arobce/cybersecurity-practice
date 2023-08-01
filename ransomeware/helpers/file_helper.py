import os

class FileHelper:
    def get_files(self):
        files = []

        for file in os.listdir("files"):
            files.append(file)

        return files

    def get_file_content(self, file_path):
        with open(file_path, "rb") as the_file:
            data = the_file.read()
        
        return data
        
    def set_file_content(self, file_path, content):
        with open(file_path, "wb") as the_file:
            the_file.write(content) 
