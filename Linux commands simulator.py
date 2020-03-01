# Importing os, shutil module
import os
import shutil
# mkdir function
def mkdir():
    # Creating folders
    # Directory
    directory = input("Enter a folder name:")
    # Parent directory path, considering that you have to use"\" in windows paths
    parent_dir = input("Type a path:")
    # Path(Parent directory path + Directory)
    path = os.path.join(parent_dir, directory)
    # Check if the directory is already exist or not
    # before making it
    if os.path.exists(path):
        print("Error, the file is already exist!")
        # Option function to return to the mkdir or to the main menu
        def option():
            answer = input("Would you like to return to the mkdir or to the main menu?:")
            if answer == "mkdir":
                mkdir()
            elif answer == "main menu":
                main_menu()
            else:
                return option()
        option()
    else:
        # Creating the directory
        os.mkdir(path)
    print("The '%s' directory has been created successfully!" % directory)
    # Return to the main menu after the execution
    return main_menu()
# rmdir function
def rmdir():
    # Removing an empty-folder
    # Directory
    directory = input("Enter a file name:")
    # Parent directory path, considering that you have to use"\" in windows paths
    parent_dir = input("Type a path:")
    # Path(Parent directory path + Directory)
    path = os.path.join(parent_dir, directory)
    # Check if the directory is already exist or not
    # before removing it
    if os.path.exists(path):
        # Removing the directory
        os.rmdir(path)
    else:
        print("Error, the file does not exist!")
        # Option function to return to the mkdir or to the main menu
        def option():
            answer = input("Would you like to return to the rmdir or to the main menu?:")
            if answer == "rmdir":
                rmdir()
            elif answer == "main menu":
                main_menu()
            else:
                return option()
        option()
    print("The '%s' directory has been removed successfully!" % directory)
    # Return to the main menu after the execution
    return main_menu()
# cat function
# Note: it creates the document files in the file project in PycharmProjects
def cat():
    # Create document files  only
    def cat_create():
        # The number of document files number
        DocNumber = int(input("How many Documents would you like to create?:"))
        for i in range(DocNumber):
            # Document name, considering the file format
            DocName = input("Enter a name of a file with its format:")
            # Creating the document file
            # Also, it checks if the file is already exist, it will erase its contents
            document_file = open(DocName, "w")
            # Close the document file
            document_file.close()
            print("Document file has been created successfully!")
            # Option function to return to the menu or to the main menu
            def option():
                answer = input("Would you like to return to the menu or to the main menu?:")
                if answer == "menu":
                    menu()
                elif answer == "main menu":
                    main_menu()
                else:
                    return option()
            option()
    # Write on document files only
    def cat_write():
        # Finding the document file and open it for writing
        document_file = open(input("Enter a file name:"), "w")
        # Write on the document file
        document_file.write(input("Type:"))
        # Close the document file
        document_file.close()
        # Option function to return to the menu or to the main menu
        def option():
            answer = input("Would you like to return to the menu or to the main menu?:")
            if answer == "menu":
                menu()
            elif answer == "main menu":
                main_menu()
            else:
                return option()
        option()
    # Read document files only
    def cat_read():
        # Finding the document file and open it for reading
        document_file = open(input("Enter file name"), "r")
        # Read the document file and print its contents
        read = document_file.read()
        print(read)
        # Option function to return to the menu or to the main menu
        def option():
            answer = input("Would you like to return to the menu or to the main menu?:")
            if answer == "menu":
                menu()
            elif answer == "main menu":
                main_menu()
            else:
                return option()
        option()
    # Add contents on document files only
    def cat_add():
        # Finding the document file and open it for appending
        document_file = open(input("Enter file name"), "a")
        # Write on the document file
        document_file.write(input(input("Type:")))
        # Close the document file
        document_file.close()
        print("Finish adding!")
        # Option function to return to the menu or to the main menu
        def option():
            answer = input("Would you like to return to the menu or to the main menu?:")
            if answer == "menu":
                menu()
            elif answer == "main menu":
                main_menu()
            else:
                return option()
        option()
    # The menu
    def menu():
        print("Pick one:")
        print("1- Create file\n 2- Write on file\n 3- Read file\n 4- Add on file")
        answer = int(input("Enter the option number:"))
        if answer == 1:
            cat_create()
        elif answer == 2:
            cat_write()
        elif answer == 3:
            cat_read()
        elif answer == 4:
            cat_add()
        else:
            return menu()
    menu()
# rm function
def rm():
    # Removing one document file only
    def remove_a_document():
        # Document name, considering the file format
        directory = input("Enter a file name:")
        # Parent directory path, considering that you have to use"\" in windows paths
        parent_dir = input("Type a path:")
        # Path(Parent directory path + Directory)
        path = os.path.join(parent_dir, directory)
        # Check if the directory is already exist or not
        # before removing it
        if os.path.exists(directory):
            os.remove(path)
        else:
            print("Error, the file does not exist!")
            # Option function to return to the menu or to the main menu
            def option():
                answer = input("Would you like to return to the rm or to the main menu?:")
                if answer == "rm":
                   rm()
                elif answer == "main menu":
                   main_menu()
                else:
                    return menu()
            option()
        print("The '%s' directory has been removed successfully!" % directory)
        def option():
            answer = input("Would you like to return to the rm or to the main menu?:")
            if answer == "rm":
                rm()
            elif answer == "main menu":
                main_menu()
            else:
                return menu()
        option()
    # Removing all the document files at the same path
    def remove_all_documents():
        # Parent directory path
        path = input("Enter a path:")
        # Looking for document files at the path
        for file in os.scandir(path):
            if file.name.endswith(".txt"):
                # Removing the document files
                os.unlink(file.path)
            else:
                print("Error, the files did not exist!")
                # Option function to return to the menu or to the main menu
                def option():
                    answer = input("Would you like to return to the menu or to the main menu?:")
                    if answer == "menu":
                        rm()
                    elif answer == "main menu":
                        main_menu()
                    else:
                        return menu()
                option()
        print("Documents have been removed successfully!")
        # Option function to return to the menu or to the main menu
        def option():
            answer = input("Would you like to return to the menu or to the main menu?:")
            if answer == "menu":
                rm()
            elif answer == "main menu":
                main_menu()
            else:
                return menu()
        option()
    # Removing non-empty folder
    def remove_nonempty_folder():
        # Directory
        directory = input("Enter a file name:")
        # Parent directory path, considering that you have to use"\" in windows paths
        parent_dir = input("Type a path:")
        # Path(Parent directory path + Directory)
        path = os.path.join(parent_dir, directory)
        # Check if the directory is already exist or not
        # before removing it
        if os.path.exists(path):
            shutil.rmtree(path)
        else:
            print("Error, the file does not exist!")
            # Option function to return to the menu or to the main menu
            def option():
                answer = input("Would you like to return to the menu or to the main menu?:")
                if answer == "menu":
                    menu()
                elif answer == "main menu":
                    main_menu()
                else:
                    return menu()
            option()
        print("The '%s' directory  has been removed successfully!" % directory)
        # Option function to return to the menu or to the main menu
        def option():
            answer = input("Would you like to return to the menu or to the main menu?:")
            if answer == "menu":
                rm()
            elif answer == "main menu":
                main_menu()
            else:
                return menu()
        option()
    # The menu
    def menu():
        print("Pick one:")
        print("1- Remove a document\n 2- Remove all documents\n 3- Remove non-empty folder")
        answer = int(input("Enter option number:"))
        if answer == 1:
            remove_a_document()
        elif answer == 2:
            remove_all_documents()
        elif answer == 3:
            remove_nonempty_folder()
        else:
            return menu()
    menu()
# mv function
def mv():
    # Rename folders or documents
    def rename_files():
        # Directory, considering that if its folder or txt file
        old_directory = input("Enter a file name:")
        # Parent directory path, considering that you have to use"\" in windows paths
        old_parent_dir = input("enter a path:")
        # Old path(Old parent Directory path + Old directory)
        old_path = os.path.join(old_parent_dir, old_directory)
        # New directory, considering that if its folder or txt file
        new_directory = input("Enter the new file name:")
        # New parent directory path
        new_parent_dir = old_path
        # New path(New parent Directory path + New directory)
        new_path = os.path.join(new_parent_dir, new_directory)
        # Check if the directory is already exist or not
        # before renaming it
        if os.path.exists(old_directory):
            os.rename(old_path, new_path)
        else:
            print("Error, the file does not exist!")
            # Option function to return to the menu or to the main menu
            def option():
                answer = input("Would you like to return to the menu or to the main menu?:")
                if answer == "menu":
                    rm()
                elif answer == "main menu":
                    main_menu()
                else:
                    return menu()
            option()
        print("The '%s' directory  has been renamed successfully!" % old_directory)
        # Option function to return to the menu or to the main menu
        def option():
            answer = input("Would you like to return to the menu or to the main menu?:")
            if answer == "menu":
                rm()
            elif answer == "main menu":
                main_menu()
            else:
                return menu()
        option()
    # Moving folders or documents
    def move_files():
        # Directory, considering that if its folder or txt file
        directory = input("Enter a file name:")
        # Old parent directory path, considering that you have to use"\" in windows paths
        old_parent_dir = input("Enter a path:")
        # Old path(Old parent Directory path + Directory)
        old_path = os.path.join(old_parent_dir, directory)
        # New parent directory path
        new_parent_dir = input("Enter the new path:")
        # New path(New parent Directory path + New directory)
        new_path = os.path.join(new_parent_dir, directory)
        # Check if the directory is already exist or not
        # before moving it
        if os.path.exists(directory):
            print("Error, the file is already exist! or there is a file having the same name")
            # Option function to return to the menu or to the main menu
            def option():
                answer = input("Would you like to return to the menu or to the main menu?:")
                if answer == "menu":
                    rm()
                elif answer == "main menu":
                    main_menu()
                else:
                    return menu()
            option()
        else:
            shutil.move(old_path, new_path)
        print("The '%s' directory  has been moved successfully!" % directory)
        # Option function to return to the menu or to the main menu
        def option():
            answer = input("Would you like to return to the menu or to the main menu?:")
            if answer == "menu":
                rm()
            elif answer == "main menu":
                main_menu()
            else:
                return menu()
        option()
    # The menu
    def menu():
        print("pick one:")
        print("1- Rename files\n 2- Move files")
        answer = int(input("Enter option number:"))
        if answer == 1:
            rename_files()
        elif answer == 2:
            move_files()
    menu()
def main_menu():
    print("***Welcome to linux command lines simulator***")
    print("----------------------------------------------")
    print("Select number of one of these commands:")
    print("1- mkdir\n 2- rmdir\n 3- cat\n 4- rm\n 5- mv")
    user = int(input("your choose:"))
    if user == 1:
        print("----------------------------------------------")
        mkdir()
        print("----------------------------------------------")
    elif user == 2:
        print("----------------------------------------------")
        rmdir()
        print("----------------------------------------------")
    elif user == 3:
        print("----------------------------------------------")
        cat()
        print("----------------------------------------------")
    elif user == 4:
        print("----------------------------------------------")
        rm()
        print("----------------------------------------------")
    elif user == 5:
        print("----------------------------------------------")
        mv()
        print("----------------------------------------------")
    else:
        return main_menu()
main_menu()











