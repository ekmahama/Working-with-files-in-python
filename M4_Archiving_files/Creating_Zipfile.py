import zipfile


to_zip = [
    './files/02_file_test.csv',
    './files/01_test.csv',
    './files/01_test_file.csv',
    './files/02_file_test.csv',
    './files/subfolder/01_file_test.csv',
    './files/subfolder/01_test_file.csv',
]

def create_zip(zipfilename, files, opt):
    with zipfile.ZipFile(zipfilename, opt, allowZip64=True) as archive:
        for f in files:
            archive.write(f)


create_zip('./files.zip', to_zip, 'w')