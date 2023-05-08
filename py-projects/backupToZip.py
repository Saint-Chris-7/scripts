#copies an entire folder and its contents into a zip file whose filename increments
import os,zipfile

def backupToZip(folder):
    #backupp the entire contents of "folder" into zipfile
    folder= os.path.abs(folder)#make sure the folder is in a absolute path
    number = 1

    while True:
        zipFilename= os.path.basename(folder)+"_"+str(number)+".zip"

        if not os.path.exists(zipFilename):
            break
        number +=1

    #Create the ZIP file.
    print('Creating %s...' % (zipFilename))
    backupZip= zipfile.ZipFile("zipFilename","w")
    #walk the entire folder and compress the files 

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_' 
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print("Done")


