from helper import FileSystem  
def main():
    fs = FileSystem("/home/ritwiz/Desktop/commvault")

    while True:
        print("Options:")
        print("1. Create File")
        print("2. Edit File")
        print("3. Delete File")
        print("4. Get File Details")
        print("5. Revert to Version")
        print("6. Copy File")
        print("7. Move File")
        print("8. Append To File")
        print("9. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            file_name = input("Enter the file name: ")
            content = input("Enter the file content: ")
            fs.create_file(file_name, content)
        elif choice == "2":
            file_name = input("Enter the file name: ")
            new_content = input("Enter the new content: ")
            fs.edit_file(file_name, new_content)
        elif choice == "3":
            file_name = input("Enter the file name: ")
            fs.delete_file(file_name)
        elif choice == "4":
            file_name = input("Enter the file name: ")
            fs.get_details(file_name)
        elif choice == "5":
            file_name = input("Enter the file name: ")
            version_number = int(input("Enter the version number: "))
            fs.revert_to_version(file_name, version_number)
        elif choice == "6":
            file_name = input("Enter the file name: ")
            new_path = input("Enter the destination path: ")
            fs.copy_file(file_name, new_path)
        elif choice == "7":
            file_name = input("Enter the file name: ")
            new_path = input("Enter the destination path: ")
            fs.move_file(file_name, new_path)
        elif choice == "8":
            file_name = input("Enter the file name: ")
            new_content = input("Enter the new content which is to be appended: ")
            fs.append_to_file(file_name, new_content)
        elif choice =='9':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
