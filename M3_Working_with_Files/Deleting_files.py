import os

def remove_files(f):
    if os.path.isfile(f):
        try:
            os.remove(f)
        except OSError as e:
            print(f"Error: {f} : {e.strerror}")   
    else:
        print(f"Error: {f} is not a valid file")


remove_files("./files/text.txt")