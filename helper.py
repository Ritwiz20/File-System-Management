import os 
import shutil
import datetime

class FileSystem:

    def __init__(self, base_directory):
        self.base_directory = base_directory
        self.file_system = {}
        self.versions = {}
        self.current_version = 1

        if not os.path.exists(self.base_directory):
            os.makedirs(self.base_directory)

    
    def get_details(self, file_name):
        file_path = os.path.join(self.base_directory, f"{file_name}.txt")
        if os.path.exists(file_path):
            print("File System : ", self.file_system[file_name])
            print("Versions : ", self.versions[file_name])
            print("Current Version : ", self.file_system[file_name]['version'])

            file_system_details = f"File System : {self.file_system[file_name]}\n"
            versions_details = f"Versions : {self.versions[file_name]}\n"
            current_version_details = f"Current Version : {self.file_system[file_name]['version']}\n"
            return file_system_details + versions_details + current_version_details
        else:
            print("File doesn't exist.")
            

    def create_file(self, file_name, content):
        file_path = os.path.join(self.base_directory, f"{file_name}.txt")
        
        if os.path.exists(file_path):
            print("File already exists.")
        else:
            self.file_system[file_name] = {
                'version': self.current_version,
                'created_at': datetime.datetime.now()
            }
            self.versions[file_name] = {self.current_version: content}
            self.current_version += 1

            with open(file_path, 'w') as file:
                file.write(content)
            print(f"File '{file_name}' created as '{file_path}'.")
            print(self.file_system)
            print(self.versions)

    
    def edit_file(self, file_name, new_content):
        file_path = os.path.join(self.base_directory, f"{file_name}.txt")
   
        if os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write(new_content)

            self.file_system[file_name]['version'] += 1
            self.file_system[file_name]['created_at'] = datetime.datetime.now()
            version = self.file_system[file_name]['version']
            self.current_version = version
            self.versions[file_name][version] = new_content
            
            print(f"File '{file_name}' content has been updated to version {version}.")
            print(self.file_system)
            print(self.versions)
        else:
            print(f"File '{file_name}' not found in the directory.")


    def append_to_file(self, file_name, new_content):
        file_path = os.path.join(self.base_directory, f"{file_name}.txt")

        if os.path.exists(file_path):
            with open(file_path, 'a') as f:
                f.write(new_content)

            self.file_system[file_name]['version'] += 1
            self.file_system[file_name]['created_at'] = datetime.datetime.now()
            version = self.file_system[file_name]['version']
            self.current_version = version

            with open(file_path, 'r') as f:
                to_be_updated = f.read()

            self.versions[file_name][version] = to_be_updated

            print(f"File '{file_name}' content has been altered.")
            print(self.file_system)
            print(self.versions)
        else:
            print(f"File '{file_name}' not found in the directory.")


    def delete_file(self, file_name):
        file_path = os.path.join(self.base_directory, f"{file_name}.txt")
        print(file_path)
        if os.path.exists(file_path):
            os.remove(file_path)
            del self.file_system[file_name]
            del self.versions[file_name]
            self.current_version = 0
            print(f"Deleted {file_name}.txt successfully!")
        else:
            print("No such file found to delete.")

    
    # def revert_to_version(self, file_name, version_number):
    #     file_path = os.path.join(self.base_directory, f"{file_name}.txt")
    #     print(file_path)

    #     if os.path.exists(file_path):
    #         updated_content = self.versions[file_name][version_number]
    #         print(updated_content)

    #         with open(file_path, 'w') as f:
    #             f.write(updated_content)
    #             print(f"File {file_name} has been reverted to version {version_number}")

    #         self.file_system[file_name]['version'] = version_number
    #         self.file_system[file_name]['created_at'] = datetime.datetime.now()
    #     else:
    #         print("File not found")


    def revert_to_version(self, file_name, version_number):

        file_path = os.path.join(self.base_directory, f"{file_name}.txt")

        if os.path.exists(file_path):
            try:
                if self.versions[file_name][version_number]:
                    load_content = self.versions[file_name][version_number]  
            except KeyError:
                print(f"For the file {file_name}, there is no version {version_number}, Try another version number")
            else:
                with open(file_path, 'w') as f:
                    f.write(load_content)
                    
                self.file_system[file_name]['version'] = version_number
                self.file_system[file_name]['created_at'] = datetime.datetime.now()
                print(f"{file_name} has been reverted back to version {version_number}")     
        else:
            print(f"{file_name} not found")



    def copy_file(self, file_name, new_path):
        file_path = os.path.join(self.base_directory, f"{file_name}.txt")
        print(file_path)

        if os.path.exists(file_path):
            new_file_path = os.path.join(new_path, f"{file_name}(Copy).txt")
            shutil.copy(file_path, new_file_path)
            print(f"{file_name} has been copied to {new_path} with the name {new_file_path.split('/')[-1]}")
        else:
            print("File not found which can be copied.") 


    def move_file(self, file_name, new_path):
        file_path = os.path.join(self.base_directory,f"{file_name}.txt")
        new_file_path = os.path.join(new_path, f"{file_name}.txt")

        if os.path.exists(file_path):
            if os.path.exists(new_file_path):
                print(f"File {file_name} already exists in {new_path}")
            else:
                shutil.move(file_path, new_file_path)
                print(f"{file_name} has been copied to {new_path}")
        else:
            print("No file found which can be moved")