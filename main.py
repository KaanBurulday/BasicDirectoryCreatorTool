import os
import shutil

# This is a tool for making creating multiple folders with the same name simpler.
# ex.: for a course of 14 weeks, creating 14 folders can be boring at times.

directory_path_root = ""
directory_name = "Week"
directory_count = 11
directory_start_count = 1
directory_path = f"{directory_path_root}\\{directory_name}"

def remove_directory(remove_directory_path):
    try:
        shutil.rmtree(remove_directory_path)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))

def exit_tool():
    print("Exited.")
    exit()

print("To exit at any point, please input 'X'")

input_create_confirmation = input(f"This is an example of the directory that will be created: "
                   f"{directory_path} {directory_start_count}"
                   "\nAre you sure? (Y/N): ")

input_create_confirmation_safety_counter = 10
if (input_create_confirmation.lower() == "n" or directory_path_root is None) and input_create_confirmation.lower() != "x":
    if directory_path_root is None:
        print(f"Directory root path ({directory_path_root}) is not valid.")
    for i in range(input_create_confirmation_safety_counter):
        directory_path_root = input("Please enter the new directory root: ")
        exit_tool() if directory_path_root == "x" else None
        directory_name = input("Please enter directory name: ")
        exit_tool() if directory_name == "x" else None
        directory_path = f"{directory_path_root}\\{directory_name}"
        input_create_confirmation = input(f"This is an example of the directory that will be created: "
                                          f"{directory_path} {directory_start_count}"
                                          "\nAre you sure? (Y/N): ")
        if not os.path.exists(directory_path_root) or directory_start_count is None:
            print("Directory does not exist. Please try again.")
        elif input_create_confirmation.lower() == "x" or input_create_confirmation.lower() == "y":
            break
        if i == input_create_confirmation_safety_counter - 1:
            input_create_confirmation = "x"

if input_create_confirmation.lower() == "x":
    exit_tool()
    
ask_again = True
overwrite = False
if input_create_confirmation.lower() == "y":
    for i in range(directory_start_count, directory_count + 1):
        directory_to_create_path = f"{directory_path} {i}"
        if os.path.exists(directory_to_create_path):
            if ask_again:
                input_file_exists_action = input(f"The directory {directory_to_create_path} already exists."
                                                 f"\n1. Do nothing."
                                                 f"\n2. Do for all possible occurrences."
                                                 f"\n3. Overwrite (removes all information inside)"
                                                 f"\n4. Overwrite for all possible occurrences."
                                                 f"\nWhat would you like to do? (Enter the option number): ")
                if input_file_exists_action == "x":
                    exit_tool()
                if input_file_exists_action.lower() == "1":
                    continue
                elif input_file_exists_action.lower() == "2" or input_file_exists_action.lower() == "4":
                    ask_again = False
                elif input_file_exists_action.lower() == "3" or input_file_exists_action.lower() == "4":
                    overwrite = True
            else:
                if overwrite:
                    remove_directory(directory_to_create_path)
                else:
                    continue
        else:
            os.mkdir(directory_to_create_path)
    print("Directory created successfully")
    os.startfile(f"{directory_path_root}")
else:
    print("Directory not created")
    exit_tool()

