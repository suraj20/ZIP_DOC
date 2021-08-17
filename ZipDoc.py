
"""
Created on Tue Aug 17-2021 19:40
@author: Suraj
"""
import os
import shutil

############################
global folderName
############################

folderName = input('Enter the folder name: ')
os.chdir(folderName)
newpath = folderName + '\\' + 'DOCForZip'
os.makedirs(newpath)

for root, dirs, files in os.walk(folderName):
    for f in files:
        zz = os.path.join(root, f)
        ext = zz.split(".")
        if ext[-1] == 'docx':
            print(f)
            try:
                shutil.copy2(zz, newpath)  # file(image_path, newpath)
            except shutil.SameFileError:
                pass

shutil.make_archive('DocZipped', 'zip', 'DOCForZip')
print("Completed")
try:
    shutil.rmtree(newpath)
except OSError as e:
    print("Error: %s - %s." % (e.filename, e.strerror))
exit()
