import zipfile

to_add = [
    'files/01_file.csv',
    'files/01_file.txt'
]

def add_to_zip(zipf, files, opt):
    with zipfile.ZipFile(zipf, opt) as archive:
        for f in files:
            lst = archive.namelist()
            if not f in lst:
                archive.write(f)
            else:
                print(f'File exist in zip : {f}')

add_to_zip('./files.zip', to_add, 'a')