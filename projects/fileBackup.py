# #backup.py Is a script for backing up files
import os,zipfile

def backupZip(folder):
    
    folder = os.path.abspath(folder) #make sure the folder path is absolute
    counter = 1

    #figure out the file name and if it exists
    while True:
        zipfilename = os.path.basename(folder)+str(counter)+".zip"

        if not os.path.exists(zipfilename):
            break
        counter += 1
    # TODO: Create the ZIP file.
    print(f"The {zipfilename} is being created")

    zip = zipfile.ZipFile(zipfilename,"w")
    for filedir,foldername,filename in os.walk(folder):
        zip.write(foldername)
        for file in filename:
            newBase = os.path.basename(folder) + '_'
            if file.startswith(newBase) and file.endswith(".zip"):
                continue
            zip.write(os.path.join(foldername,file))
        zip.close()
        print("close")
path = r"C:\Users\HP\Documents\Dev\Pyscripts\generator\excercise-1.py"
backupZip(path)


# #! python3
# import zipfile, os
# def backupToZip(folder):
#     # Backup the entire contents of "folder" into a ZIP file.
#     folder = os.path.abspath(folder) # make sure folder is absolute
#     # Figure out the filename this code should use based on
#     # what files already exist.
#     number = 1
#     while True:
#         zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
#         if not os.path.exists(zipFilename):
#             break
#             number = number + 1
#             print('Creating %s...' % (zipFilename))
#         backupZip = zipfile.ZipFile(zipFilename, 'w')
#         # Walk the entire folder tree and compress the files in each folder.
#         for foldername, subfolders, filenames in os.walk(folder):
#             print('Adding files in %s...' % (foldername))
#         # Add the current folder to the ZIP file.
#             backupZip.write(foldername)
#         # Add all the files in this folder to the ZIP file.
#             for filename in filenames:
#                 newBase = os.path.basename(folder) + '_' 
#                 if filename.startswith(newBase) and filename.endswith('.zip'):
#                     continue # don't backup the backup ZIP files
#                 backupZip.write(os.path.join(foldername, filename))
#         backupZip.close()
#     print('Done.')
# backupToZip(r""C:\Users\HP\Documents\Dev\Pyscripts\generator\excercise-1.py"")