from distutils.command.build_ext import extension_name_re
import os
import shutil
global path
# initialzing a set() to save extesions
extensions_set= set()

# address of directory
path = input('enter your path :')
files_list = os.listdir(path)

# extracting the extension of files and add to Set()
for each_file in files_list:
    extension =os.path.splitext(each_file)[1]
    extensions_set.add(extension)

print('the file types are:',extensions_set)

# create folders base on extensions
try:
    for x in extensions_set:
        directory = os.path.join(path,x)
        isExist = os.path.exists(directory)
        if isExist ==False:
            os.makedirs(directory+'_files')
        elif isExist== True:
            print('folders are exist')
            input()
 # Move files to folders
    for each_file in files_list:
        extension =os.path.splitext(each_file)[1]
        src = os.path.join(path,each_file)  
        dst = os.path.join(path,extension)
        shutil.move(src,dst+'_files')
        print('files moved and ordered')
    
except:
    print('try again, something went wrong')
    input()
