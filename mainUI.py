import customtkinter
from loguru import logger
import os
import requests

Icon = "Icon"
if os.path.exists(Icon):
    print("'Icon' folder already exists")
else:
    print("Creating Icon folder")
    os.makedirs(Icon)
    print("'Icon' folder created")

def download_ico(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print("ICO file downloaded successfully!")
    else:
        print("Failed to download ICO file.")

url = "https://raw.githubusercontent.com/Bernso/Icons/main/Arhururan.ico"
save_path = os.path.join(Icon, "Arhururan.ico")  # Full file path including directory
download_ico(url, save_path)

def show_info(title, message):
    top = customtkinter.CTkToplevel()
    top.title(title)
    label = customtkinter.CTkLabel(top, text=message)
    label.pack(padx=10, pady=10)
    ok_button = customtkinter.CTkButton(top, text="OK", command=top.destroy)
    ok_button.pack(padx=10, pady=10)

def show_error(title, message):
    top = customtkinter.CTkToplevel()
    top.title(title)
    label = customtkinter.CTkLabel(top, text=message)
    label.pack(padx=10, pady=10)
    ok_button = customtkinter.CTkButton(top, text="OK", command=top.destroy)
    ok_button.pack(padx=10, pady=10)

def create_folders():
    try:
        folders_to_create = int(entry.get()) + 1
        for i in range(1, folders_to_create):
            folder_name = str(i)
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
                file_path = os.path.join(folder_name, 'Beans.txt')
                with open(file_path, 'w') as file:
                    for _ in range(1, 1000):
                        file.write(f"Beans No.{folder_name}\n")
                logger.success(f"Folder {folder_name} successfully created")
            else:
                logger.error(f"Folder {folder_name} already exists")
        show_info("Success", "Folders created successfully!")
    except ValueError:
        show_error("Error", "ERROR\nPlease enter a valid number.")

# GUI setup
root = customtkinter.CTk()
root.geometry('350x200')
root.title("Folder Creator")
root.iconbitmap(r"Icon\Arhururan.ico")

label = customtkinter.CTkLabel(root, text="Enter the number of folders you would like to create:")
label.pack(padx=10, pady=10)

entry = customtkinter.CTkEntry(root)
entry.pack(padx=10, pady=10)

create_button = customtkinter.CTkButton(root, text="Create Content", command=create_folders)
create_button.pack(padx=10, pady=10)

exit_button = customtkinter.CTkButton(root, text="Close", command=exit)
exit_button.pack(padx=10, pady=10)

root.mainloop()
