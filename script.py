import os
import shutil
from itertools import zip_longest
import datetime as dt

# Declaring variables as global so that it can be used in the function compare()
global acad_dirs_list
global new_dirs_list
global datetime_file_name

x = dt.datetime.now()
datetime_file_name = x.strftime("%d-%m-%y_%H-%M.txt")   # Declaring a string with the datetime stamp
acad_dirs_list = os.listdir("./AutoCAD_Versions/")   # Storing names of all directories in a list


# Declaring and Initializing a list that will contain the new directories in new_dirs_list
new_dirs_list = []
for acad_dir in acad_dirs_list:
    new_dir = "DF_" + acad_dir
    new_dirs_list.append(new_dir)

# Declaring and Initializing a list that will contain the old directories in old_dirs_list
old_dirs_list = []
for new_dir in new_dirs_list:
    old_dirs_list.append(new_dir + "_old")

def compare(dir1, dir2):
    from filecmp import dircmp
    global datetime_file_name
    file = open("./" + new_dir + "/" + datetime_file_name, "a")

    global acad_dirs_list
    global new_dirs_list

    comparison = dircmp(dir1, dir2, ignore=None)
    for i in comparison.right_only:
        file.write("Added: " + dir2 +"/"+ i + "\n")

    for i in comparison.left_only:
        file.write("Removed: " + dir2 +"/"+ i + "\n")

    for i in comparison.diff_files:
        file.write("Modified: " + dir2 +"/"+ i + "\n")

    for i in comparison.common_dirs:
        new_dir1 = dir1 + "/" + i
        new_dir2 = dir2 + "/" + i
        compare(new_dir1, new_dir2)

    file.close()

for acad_dir,old_dir,new_dir in zip_longest(acad_dirs_list,old_dirs_list,new_dirs_list,fillvalue=None):
    print()  # Adding a line between operations on each version

    # Removing DF_2011_old directories
    shutil.rmtree(os.path.join("./", old_dir), ignore_errors=True)
    print((old_dir + " deleted"))

    # DF_2011 copied to DF_2011_old
    src = new_dir
    dest = "./" + new_dir + "_old" shutil.move(src, dest, copy_function=shutil.copy2)
    print((src + " copied to " + dest + ""))

    # Copying DF to DF_2011
    des_dir = "./" + new_dir
    shutil.copytree("./DF", des_dir, dirs_exist_ok=True)
    print((new_dir + " directory updated/copied"))

    # Copying contents of AutoCAD_Versions/2011 to DF_2011/ra/Resources/
    src_dir = "./AutoCAD_Versions/" + acad_dir
    des_dir = "./DF_" + acad_dir + "/ra/Resources"
    shutil.copytree(src_dir, des_dir, copy_function=shutil.copy, dirs_exist_ok=True)
    print("Contents of AutoCAD_Versions/" + acad_dir + " copied to DF_" + acad_dir + "/ra/Resources/" + "")


    # Creating a file with the time stamp as the file name. Doesn't work if the file already exists.
    box = open("./" + new_dir + "/" + datetime_file_name, "x")
    box.close()

    # Calling the compare function to comparing the directory structures
    dir_left = new_dir + "_old"
    dir_right = new_dir
    compare(dir_left, dir_right)

    shutil.make_archive(new_dir, "zip", new_dir)  # Creating zip file
    print((new_dir + " compressed into " + new_dir + ".zip" + ""))  # Notifying creation of zip
    os.remove("./" + new_dir + "/" + datetime_file_name)  # Removing timestamp file after zip creation

    for i in range(3):
        print("Hello World!")
