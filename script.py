import os

def copy_files():
    import shutil

    acad_dirs_list = os.listdir("./AutoCAD_Versions/")  # Storing names of all directories in a list

    new_dir_list = []  # Declaring a list that will contain all the new directories

    for i in acad_dirs_list:  # Initializing new_dir_list
        new_dir = "DF_" + i
        new_dir_list.append(new_dir)

    for i in new_dir_list:  # Copying DF to DF_2011
        des_dir = "./" + i
        shutil.copytree("./DF", des_dir, dirs_exist_ok=True)  # dirs_exist_ok=True doesn't break the code if the directories already exist.
        text_block.insert(INSERT, (i + " directory updated/copied\n"))

    text_block.insert(INSERT, "\n")
    for i in acad_dirs_list:  # Copying contents of AutoCAD_Versions/2011 to /Resources/
        src_dir = "./AutoCAD_Versions/" + i
        des_dir = "./DF_" + i + "/ra/Resources"
        shutil.copytree(src_dir, des_dir, copy_function=shutil.copy, dirs_exist_ok=True)
        text_block.insert(INSERT, ("Contents of AutoCAD_Versions/" + i + " copied to DF_" + i + "/ra/Resources/" + "\n"))

def zip_files():
    import shutil

    import datetime as dt

    acad_dirs_list = os.listdir("./AutoCAD_Versions/")  # Storing names of all directories in a list

    new_dir_list = []  # Declaring a list that will contain all the new directories

    for i in acad_dirs_list:  # Initializing new_dir_list
        new_dir = "DF_" + i
        new_dir_list.append(new_dir)

    x = dt.datetime.now()

    datetime_file_name = x.strftime("%d") + "-" + x.strftime("%m") + "-" + x.strftime("%y") + "_" + x.strftime(
        "%H") + "-" + x.strftime("%M") + ".txt"
    for i in new_dir_list:  # Creating a file with the time stamp as the file name. Doesn't work if the file already exists.
        open("./" + i + "/" + datetime_file_name, "x")

    text_block.insert(INSERT, "\n")
    for i in new_dir_list:  # Creating zip file
        shutil.make_archive(i, "zip", i)
        text_block.insert(INSERT, (i + " compressed into " + i + ".zip" + "\n"))
        os.remove("./" + i + "/" + datetime_file_name)  # Removing timestamp file after zip creation

def compare_files():
    import filecmp

    acad_dirs_list = os.listdir("./AutoCAD_Versions/")  # Storing names of all directories in a list

    new_dir_list = []  # Declaring a list that will contain all the new directories

    for i in acad_dirs_list:  # Initializing new_dir_list
        new_dir = "DF_" + i
        new_dir_list.append(new_dir)

    for i in new_dir_list:
        dir1 = "./DF_old"
        dir2 = i
        comparison = filecmp.cmp(dir1, dir2, shallow=True)
        text_block.insert(INSERT, comparison)

from tkinter import *

root = Tk()

# GUI layout

copy_button = Button(root, command=copy_files, text="Copy", width=20, height=5)
copy_button.grid(row=0, column=0, ipadx=15)

zip_button = Button(root, command=zip_files, text="Zip", width=20, height=5)
zip_button.grid(row=0, column=1, ipadx=15)

compare_button = Button(root, command=compare_files, text="Compare", width=20, height=5)
compare_button.grid(row=0, column=2, ipadx=15)

text_width = 60 + 45
text_block = Text(root, width=text_width, font="Helvetica")
text_block.grid(row=1, column=0, columnspan=3, ipadx=0)

root.mainloop()
