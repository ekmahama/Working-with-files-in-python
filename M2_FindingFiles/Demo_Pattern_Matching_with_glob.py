import os
from pathlib import Path

# With this approach we avoid having to list the content of the directory
def glob_match(fld:str, search:str):
    p = Path(fld)
    for fn in p.glob(search):
        print(fn)


# glob_match("./files","*2*.t*")
glob_match("./files/subfolder","*_file_*.t*")