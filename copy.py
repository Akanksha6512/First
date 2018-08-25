**This is one change**

''' This Program is used to copy files from one directory to another
    by knowing the  source, destination and extension of the files
    this program also deletes the folder in the end based on user's choice '''


### IMPORT OS --> OS MODULE, SHUTIL --> SHELL_UTILITY MODULE ###
# OS -> MAKE,CHANGE,REMOVE DIRECTORIES
# SHUTIL -> COPY FILES FROM ONE DIR TO ANOTHER DIR, REMOVE NON-EMPTY DIRS

import os, shutil

source = raw_input("Enter the path of Source Directory: ") # INPUT SOURCE DIR
dest = raw_input("Enter the path of the destination: ")    # INPUT DESTINATION DIR
name = raw_input("Enter the new directory name: ")         # INPUT NAME OF NEW FOLDER
ext = raw_input("Enter the extension of the files to be transfered: ") # INPUT EXTENSION OF THE FILE

print "\n\n"


os.chdir(source)                    # SET CURRENT DIR AS SOURCE DIR
for filename in os.listdir(source):
    if filename.endswith(ext):
        print filename              # LIST THE FILES IN SOURCE WITH EXT EXTENSION

inp = raw_input("Should I proceed to move files[y/n]: ")
if inp == 'n':
    print "Alright, Files will not be moved"
elif inp =='y':
    os.chdir(dest)                  # SET CURRENT DIR AS DESTINATION DIR
    os.mkdir(name)                  # CREATE NEW FOLDER IN DESTINATION FOLDER
    os.chdir(source)                # SET CURRENT DIR AS SOURCE DIR
    for filename in os.listdir(source):
        if filename.endswith(ext):
            shutil.copy(filename,dest+'\\'+name)    # COPY TO DEST + NEWFOLDER PATH

choice = raw_input("\n\n As the test is over, do you want to delete the file[y/n]: ")

if choice == 'y':                   # ONCE CONFIRMED YOU CAN REMOVE THE NEW FOLDER
    shutil.rmtree(dest+'\\'+name)
    print "\n File "+name+" is succesfully removed"

print "\n Thank you for using Nyanmaru DB"
    
    
    
