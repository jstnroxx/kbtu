import shutil
import os

# 4. Copy and back up files using shutil.
FILE_TO_BACKUP = "sample.txt"
BACKUP_DESTINATION = "file-backupss"

if not os.path.exists(FILE_TO_BACKUP):
    open(FILE_TO_BACKUP, "x")

if not os.path.exists(BACKUP_DESTINATION):
    os.mkdir(BACKUP_DESTINATION)
    
try:
    shutil.copy2(FILE_TO_BACKUP, BACKUP_DESTINATION)    # Full file copy. (including metadata)
    print(f'Successfuly backed up "{FILE_TO_BACKUP}" to "{BACKUP_DESTINATION}"')
except:
    print(f'Something went wrong when backing up "{FILE_TO_BACKUP}".')
    
# 5. Delete files safely.
FILE_TO_DELETE = FILE_TO_BACKUP

if os.path.exists(FILE_TO_DELETE):
    print("abc")
else:
    print(f'File "{FILE_TO_DELETE}" doesn\'t exist')