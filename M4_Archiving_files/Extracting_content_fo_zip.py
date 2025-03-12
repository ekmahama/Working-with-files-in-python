import zipfile

def extract_file(zipf, fn, path):
    with zipfile.ZipFile(zipf, 'r') as archive:
        archive.extract(fn, path)

def extract_all_files(zipf, path):
    with zipfile.ZipFile(zipf, 'r') as archive:
        archive.extractall(path)


# extract_file('./files.zip', 'files/01_file.csv', 'extracted')
extract_all_files('./files.zip', 'extractedall')