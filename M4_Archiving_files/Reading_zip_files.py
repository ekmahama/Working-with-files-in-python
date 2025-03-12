import zipfile

def read_zip(zipf):
    with zipfile.ZipFile(zipf, 'r') as archive:
        lst = archive.namelist()
        for l in lst:
            zfinfo = archive.getinfo(l)
            print(f'{l} => {zfinfo.file_size} bytes, {zfinfo.compress_size}')

read_zip('./files.zip')