import shutil

def copy_files(src, dst):
    shutil.copy(src, dst)

def copy_folders(src, dst):
    shutil.copytree(src, dst)



#copy_files("./files/02_file.txt", "./files/subfolder")
copy_folders("./files", "./files/new_flder")