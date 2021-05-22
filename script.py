import os
import shutil

acad_dirs_list = os.listdir("./Acad_Versions/") # Storing names of all directories in a list

new_dir_list = [] # Declaring a list that will contain all the new directories

for i in acad_dirs_list: # Initializing new_dir_list
    new_dir = "DF_" + i
    new_dir_list.append(new_dir)

for i in new_dir_list:
    des_dir = "./" + i
    shutil.copytree("./DF", des_dir, dirs_exist_ok=True) # dirs_exist_ok=True doesn't break the code if the directories already exist.

print("\n'DF_version' directories created.")


for i in acad_dirs_list:
    src_dir = "./Acad_Versions/" + i
    des_dir = "./DF_" + i + "/RA/Resources"
    shutil.copytree(src_dir, des_dir, copy_function = shutil.copy, dirs_exist_ok=True)
print("Content from version directories copied to 'DF_version/RA/Resources/")