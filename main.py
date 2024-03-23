import os

# Asking how many times the user would like to create folders
folders_to_create = int(input("Enter the number of folders you would like to create: ")) + 1

# Starting the proccess of creating the folders for however many times the user said to do
for i in range(1, folders_to_create):
    folder_name = str(i)
    
    # What happens when the path does not exist
    if not os.path.exists(folder_name):
        
        os.makedirs(folder_name)
        print(f"Folder {folder_name} successfully created")

        # Naming the file
        file_path = os.path.join(folder_name, 'Beans.txt')
        # Creates a text file
        with open(file_path, 'w') as file:
            # Creates 1000 lines of content
            for _ in range(1, 1000):
                file.write(f"Beans No.{folder_name}\n")
    
    # What happens when the path already exists
    else:
        print(f"Folder {folder_name} already exists")

# What happens once all the folder creation and file creation is complete
print("\nThanks")
