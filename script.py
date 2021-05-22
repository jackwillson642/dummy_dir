import os
import shutil

acad_dirs_list = os.listdir("./Acad_Versions/") # Storing names of all directories in a list

new_dir_list = [] # Declaring a list that will contain all the new directories

for i in acad_dirs_list: # Initializing new_dir_list
    new_dir = "DF_" + i
    new_dir_list.append(new_dir)

print()
for i in new_dir_list: # Copying DF to DF_2011
    des_dir = "./" + i
    shutil.copytree("./DF", des_dir, dirs_exist_ok=True) # dirs_exist_ok=True doesn't break the code if the directories already exist.
    print(i+" directory updated")

print()
for i in acad_dirs_list: # Copying contents of Acad_Versions/2011 to /Resources/
    src_dir = "./Acad_Versions/" + i
    des_dir = "./DF_" + i + "/ra/Resources"
    shutil.copytree(src_dir, des_dir, copy_function = shutil.copy, dirs_exist_ok=True)
    print("Contents of Acad_Versions/"+i+" copied to DF_"+i+"/ra/Resources/")

print()
for i in new_dir_list:
    shutil.make_archive(i, "zip", i)
    print(i +" compressed into " + i + ".zip")