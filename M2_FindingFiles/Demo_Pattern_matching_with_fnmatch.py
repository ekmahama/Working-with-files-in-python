import os, fnmatch

def match(fld: str, search: str):
    for fn in os.listdir(fld):
        if fnmatch.fnmatch(fn, search):
            print(fn)


#match("./files", "*.csv")
#match("./files", "*_file.csv")
match("./files", "*1*_file.csv")