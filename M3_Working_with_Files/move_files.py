import shutil

def mv_files(src, dst):
    shutil.move(src, dst)


mv_files("./files/text.txt", "./files/subfolder/text.txt")