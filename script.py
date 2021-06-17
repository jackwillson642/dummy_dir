import os
import shutil

global acad_dirs_list
global new_dirs_list

# Storing names of all directories in a list
acad_dirs_list = os.listdir("./AutoCAD_Versions/")

new_dirs_list = []  # Declaring a list that will contain all the new directories

for acad_dir in acad_dirs_list:  # Initializing news_dir_list
    new_dir = "DF_" + acad_dir
    new_dirs_list.append(new_dir)


old_dirs_list = []  # Declaring a list that will contain all the old directories
for new_dir in new_dirs_list:  # Initializing old_dirs_list
    old_dirs_list.append(new_dir + "_old")

# Removing DF_2011_old directories
print("")
for old_dir in old_dirs_list:
    shutil.rmtree(os.path.join("./", old_dir), ignore_errors=True)
    print((old_dir + " deleted"))

# DF_2011 copied to DF_2011_old
print("")
for new_dir in new_dirs_list:
    src = new_dir
    dest = "./" + new_dir + "_old"
    shutil.move(src, dest, copy_function=shutil.copy2)
    print((src + " copied to " + dest + ""))

# Copying DF to DF_2011
for new_dir in new_dirs_list:
    des_dir = "./" + new_dir
    shutil.copytree("./DF", des_dir, dirs_exist_ok=True)
    print((new_dir + " directory updated/copied"))

# Copying contents of AutoCAD_Versions/2011 to DF_2011/ra/Resources/
print("")
for acad_dir in acad_dirs_list:
    src_dir = "./AutoCAD_Versions/" + acad_dir
    des_dir = "./DF_" + acad_dir + "/ra/Resources"
    shutil.copytree(src_dir, des_dir,
                    copy_function=shutil.copy, dirs_exist_ok=True)
    print("Contents of AutoCAD_Versions/" + acad_dir + " copied to DF_" + acad_dir + "/ra/Resources/" + "")


def compare(dir1, dir2):
    from filecmp import dircmp
    global datetime_file_name
    file = open("./" + new_dir + "/" + datetime_file_name, "a")

    global acad_dirs_list
    global new_dirs_list

    # file.write("\n")
    # print("Files added:")
    comparison = dircmp(dir1, dir2, ignore=None)
    for i in comparison.right_only:
        # if os.path.isdir(i):
        #     new_dir1 = dir1 + i
        #     new_dir2 = dir2 + i
        #     compare(new_dir1, new_dir2)
        file.write("Added: " + dir2 +"/"+ i + "\n")
        # print(i)

    # file.write("\n")
    # print("Files removed:")
    for i in comparison.left_only:
        # if os.path.isdir(i):
        #     new_dir1 = dir1 + i
        #     new_dir2 = dir2 + i
        #     compare(new_dir1, new_dir2)
        file.write("Removed: " + dir2 +"/"+ i + "\n")
        # print(i)

    # file.write("\n")
    # print("Files modified:")
    for i in comparison.diff_files:
        # if os.path.isdir(i):
        #     new_dir1 = dir1 + i
        #     new_dir2 = dir2 + i
        #     compare(new_dir1, new_dir2)
        file.write("Modified: " + dir2 +"/"+ i + "\n")
        # print(i)

    for i in comparison.common_dirs:
        new_dir1 = dir1 + "/" + i
        new_dir2 = dir2 + "/" + i
        compare(new_dir1, new_dir2)
        

    file.close()

import datetime as dt

x = dt.datetime.now()

global datetime_file_name
datetime_file_name = x.strftime("%d-%m-%y_%H-%M.txt")

# Creating a file with the time stamp as the file name. Doesn't work if the file already exists.
for new_dir in new_dirs_list:
    box = open("./" + new_dir + "/" + datetime_file_name, "x")
    box.close()

for new_dir in new_dirs_list:
    dir_left = new_dir + "_old"
    dir_right = new_dir
    compare(dir_left, dir_right)

# print("")
for new_dir in new_dirs_list:
    shutil.make_archive(new_dir, "zip", new_dir)  # Creating zip file
    print((new_dir + " compressed into " + new_dir + ".zip" + ""))  # Notifying creation of zip
    os.remove("./" + new_dir + "/" + datetime_file_name)  # Removing timestamp file after zip creation
