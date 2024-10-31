import os

def print_directory_contents(directory):
    try:
        # List the contents of the directory
        contents = os.listdir(directory)
        
        # Print each item in the directory
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Change the path to the directory you want to list
directory_path = 'Practice ps'  # Current directory
print_directory_contents(directory_path)
