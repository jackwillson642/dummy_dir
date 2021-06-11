import os
import shutil

global acad_dirs_list
global new_dirs_list

acad_dirs_list = os.listdir("./AutoCAD_Versions/")  # Storing names of all directories in a list

new_dirs_list = []  # Declaring a list that will contain all the new directories

for i in acad_dirs_list:  # Initializing news_dir_list
    new_dir = "DF_" + i
    new_dirs_list.append(new_dir)


def copy_files():
    global acad_dirs_list
    global new_dirs_list

    old_dirs_list = []
    for i in new_dirs_list:
        old_dirs_list.append(i + "_old")

    text_block.insert(INSERT, "\n")
    for i in old_dirs_list:
        shutil.rmtree(os.path.join("./", i), ignore_errors=True)
        text_block.insert(INSERT, (i + " deleted\n"))

    text_block.insert(INSERT, "\n")
    for i in new_dirs_list:
        src = i
        dest = "./" + i + "_old"
        shutil.copytree(src, dest, dirs_exist_ok=False)
        text_block.insert(INSERT, (src + " copied to " + dest + "\n3"))

    for i in new_dirs_list:  # Copying DF to DF_2011
        des_dir = "./" + i
        shutil.copytree("./DF", des_dir, dirs_exist_ok=True)
        text_block.insert(INSERT, (i + " directory updated/copied\n"))

    text_block.insert(INSERT, "\n")
    for i in acad_dirs_list:  # Copying contents of AutoCAD_Versions/2011 to /Resources/
        src_dir = "./AutoCAD_Versions/" + i
        des_dir = "./DF_" + i + "/ra/Resources"
        shutil.copytree(src_dir, des_dir, copy_function=shutil.copy, dirs_exist_ok=True)
        text_block.insert(INSERT,
                          ("Contents of AutoCAD_Versions/" + i + " copied to DF_" + i + "/ra/Resources/" + "\n"))


def zip_files():
    import datetime as dt

    global acad_dirs_list
    global new_dirs_list

    x = dt.datetime.now()

    global datetime_file_name
    datetime_file_name = x.strftime("%d-%m-%y_%H-%M.txt")

    for i in new_dirs_list:  # Creating a file with the time stamp as the file name. Doesn't work if the file already exists.
        open("./" + i + "/" + datetime_file_name, "x")

    text_block.insert(INSERT, "\n")
    print("Files added:")
    for i in new_dirs_list:
        shutil.make_archive(i, "zip", i)  # Creating zip file
        text_block.insert(INSERT, (i + " compressed into " + i + ".zip" + "\n"))  # Notifying creation of zip

        dir_left = i + "_old"
        dir_right = i
        compare(dir_left, dir_right)
        # print(compare(dir_
        # left, dir_right))


#        os.remove("./" + i + "/" + datetime_file_name)  # Removing timestamp file after zip creation


def compare(dir1, dir2):
    from filecmp import dircmp
    global datetime_file_name
    file = open("./" + i + "/" + datetime_file_name, "a")

    global acad_dirs_list
    global new_dirs_list

    file.write("Files added:")
    comparison = dircmp(dir1, dir2, ignore=None)
    for j in comparison.right_only:
        if os.path.isdir(j):
            new_dir1 = dir1 + j
            new_dir2 = dir2 + j
            compare(new_dir1, new_dir2)
        file.write(j + "\n")

    file.write("Files removed:")
    for j in comparison.left_only:
        if os.path.isdir(j):
            new_dir1 = dir1 + j
            new_dir2 = dir2 + j
            compare(new_dir1, new_dir2)
        file.write(j + "\n")

    file.write("Files modified:")
    for j in comparison.diff_files:
        if os.path.isdir(j):
            new_dir1 = dir1 + j
            new_dir2 = dir2 + j
            compare(new_dir1, new_dir2)
        file.write(j + "\n")

    file.close()


from tkinter import *

root = Tk()

# GUI layout

copy_button = Button(root, command=copy_files, text="Copy", width=20, height=5)
copy_button.grid(row=0, column=0, ipadx=15)

zip_button = Button(root, command=zip_files, text="Zip", width=20, height=5)
zip_button.grid(row=0, column=1, ipadx=15)

text_width = 60 + 45
text_block = Text(root, width=text_width, font="Helvetica")
text_block.grid(row=1, column=0, columnspan=2, ipadx=0)

root.mainloop()
