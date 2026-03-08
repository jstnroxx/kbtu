import pathlib
import shutil

FILE_PARENT_PATH = pathlib.Path(__file__).parent

# 4. Move/copy files between directories.
# 4.1. Move file.
exampleFilePath = FILE_PARENT_PATH / "exampleFile.txt"

with exampleFilePath.open("w") as exampleFile:
    exampleFile.write("Some test data.")
    
exampleFileDestination = FILE_PARENT_PATH.parent

try:
    shutil.move(exampleFilePath, exampleFileDestination)
except:
    print("Something went wrong.")
    
# 4.2. Copy file.
someFolder = FILE_PARENT_PATH / "ParentFolder"
movedExampleFile = exampleFileDestination / "exampleFile.txt"

if someFolder.exists() and movedExampleFile.exists():
    shutil.copy2(movedExampleFile, someFolder)
