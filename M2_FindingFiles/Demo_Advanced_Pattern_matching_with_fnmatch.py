import os, fnmatch

def match(fld: str, search: str):
    for fn in os.listdir(fld):
        if fnmatch.fnmatch(fn, search):
            print(fn)

match("./files", "*_file*.*")
