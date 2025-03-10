import os

def ends_with(fld: str, search: str):
    for fn in os.listdir(fld):
        if fn.endswith(search):
            print(fn)


def start_with(fld: str, search:str):
    for fn in os.listdir(fld):
        if fn.startswith(search):
            print(fn)


ends_with("./files", ".txt")
ends_with("./files", ".csv")

start_with("./files", "01_test")
