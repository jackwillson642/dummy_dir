import os
import shutil


def copy_files():
    acad_dirs_list = os.listdir("./AutoCAD_Versions/")  # Storing names of all directories in a list

    new_dir_list = []  # Declaring a list that will contain all the new directories

    for i in acad_dirs_list:  # Initializing new_dir_list
        new_dir = "DF_" + i
        new_dir_list.append(new_dir)

    for i in new_dir_list:  # Copying DF to DF_2011
        des_dir = "./" + i
        shutil.copytree("./DF", des_dir,
                        dirs_exist_ok=True)  # dirs_exist_ok=True doesn't break the code if the directories already exist.
        textblock.insert(INSERT, (i + " directory updated/copied\n"))

    textblock.insert(INSERT, ("\n"))
    for i in acad_dirs_list:  # Copying contents of AutoCAD_Versions/2011 to /Resources/
        src_dir = "./AutoCAD_Versions/" + i
        des_dir = "./DF_" + i + "/ra/Resources"
        shutil.copytree(src_dir, des_dir, copy_function=shutil.copy, dirs_exist_ok=True)
        textblock.insert(INSERT, ("Contents of AutoCAD_Versions/" + i + " copied to DF_" + i + "/ra/Resources/" + "\n"))


import datetime as dt


def zip_files():
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

    textblock.insert(INSERT, ("\n"))
    for i in new_dir_list:  # Creating zip file
        shutil.make_archive(i, "zip", i)
        textblock.insert(INSERT, (i + " compressed into " + i + ".zip" + "\n"))
        os.remove("./" + i + "/" + datetime_file_name)  # Removing timestamp file after zip creation


from tkinter import *

root = Tk()

copy_button = Button(root, command=copy_files, text="Copy", padx=70, pady=20)
copy_button.grid(row=0, column=0)

zip_button = Button(root, command=zip_files, text="Zip", padx=74, pady=20)
zip_button.grid(row=0, column=1)

textblock = Text(root, width=70, font="Helvetica")
textblock.grid(row=1, column=0, columnspan=2)

root.mainloop()