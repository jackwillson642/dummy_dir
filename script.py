import os
import shutil

global acad_dirs_list
global new_dirs_list

# Storing names of all directories in a list
acad_dirs_list = os.listdir("./AutoCAD_Versions/")

new_dirs_list = []  # Declaring a list that will contain all the new directories

for i in acad_dirs_list:  # Initializing news_dir_list
    new_dir = "DF_" + i
    new_dirs_list.append(new_dir)


old_dirs_list = []
for i in new_dirs_list:
    old_dirs_list.append(i + "_old")

print("\n")
for i in old_dirs_list:
    shutil.rmtree(os.path.join("./", i), ignore_errors=True)
    print((i + " deleted\n"))

print("\n")
for i in new_dirs_list:
    src = i
    dest = "./" + i + "_old"
    shutil.copytree(src, dest, dirs_exist_ok=False)
    print((src + " copied to " + dest + "\n3"))

for i in new_dirs_list:  # Copying DF to DF_2011
    des_dir = "./" + i
    shutil.copytree("./DF", des_dir, dirs_exist_ok=True)
    print((i + " directory updated/copied\n"))

print("\n")
for i in acad_dirs_list:  # Copying contents of AutoCAD_Versions/2011 to /Resources/
    src_dir = "./AutoCAD_Versions/" + i
    des_dir = "./DF_" + i + "/ra/Resources"
    shutil.copytree(src_dir, des_dir,
                    copy_function=shutil.copy, dirs_exist_ok=True)
    print("Contents of AutoCAD_Versions/" + i + " copied to DF_" + i + "/ra/Resources/" + "\n")


def compare(dir1, dir2):
    from filecmp import dircmp
    global datetime_file_name
    file = open("./" + i + "/" + datetime_file_name, "a")

    global acad_dirs_list
    global new_dirs_list

    file.write("Files added:")
    # print("Files added:")
    comparison = dircmp(dir1, dir2, ignore=None)
    for j in comparison.right_only:
        if os.path.isdir(j):
            new_dir1 = dir1 + j
            new_dir2 = dir2 + j
            compare(new_dir1, new_dir2)
        file.write(j + "\n")
        # print(j + "\n")

    file.write("Files removed:")
    # print("Files removed:")
    for j in comparison.left_only:
        if os.path.isdir(j):
            new_dir1 = dir1 + j
            new_dir2 = dir2 + j
            compare(new_dir1, new_dir2)
        file.write(j + "\n")
        # print(j + "\n")

    file.write("Files modified:")
    # print("Files modified:")
    for j in comparison.diff_files:
        if os.path.isdir(j):
            new_dir1 = dir1 + j
            new_dir2 = dir2 + j
            compare(new_dir1, new_dir2)
        file.write(j + "\n")
        # print(j + "\n")

    file.close()

import datetime as dt

x = dt.datetime.now()

global datetime_file_name
datetime_file_name = x.strftime("%d-%m-%y_%H-%M.txt")

# Creating a file with the time stamp as the file name. Doesn't work if the file already exists.
for i in new_dirs_list:
    box = open("./" + i + "/" + datetime_file_name, "x")
    box.close()

print("\n")
for i in new_dirs_list:
    shutil.make_archive(i, "zip", i)  # Creating zip file
    # Notifying creation of zip
    print((i + " compressed into " + i + ".zip" + "\n"))

    dir_left = i + "_old"
    dir_right = i
    compare(dir_left, dir_right)

    os.remove("./" + i + "/" + datetime_file_name)  # Removing timestamp file after zip creation
