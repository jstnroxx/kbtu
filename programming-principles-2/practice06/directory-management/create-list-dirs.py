import pathlib

FILE_PARENT_PATH = pathlib.Path(__file__).parent

# 1. Create nested directories.
newFolders = FILE_PARENT_PATH / "ParentFolder" / "NestedFolder1" / "NestedFolder2"
newFolders.mkdir(parents = True, exist_ok = True)   # "parents=True" creates every needed intermediate directory, while "exist_ok=True" prevents an exception from rising if a directory is present.

# 2. List files and folders.
for entry in FILE_PARENT_PATH.iterdir():
    print(entry.name)

# 3. Find files by extension.
extension = input('File extension (e.g. ".py"): ')

for file in FILE_PARENT_PATH.glob(f'*{extension}'):
    print(file.name)
    