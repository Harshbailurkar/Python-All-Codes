# to rename the files in the folder

import os

# C:\PROGRAMMING HARSH\adata\tutorial 1
path = input("enter the path of folder : ")

os.chdir(path)

print(os.getcwd())

print(len(os.listdir()))

for count, f in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(f)
    f_name = str(count)
    
    print(os.path.splitext(f))
    if (f_ext == ".png" ):
        new_name = f'{f_name}{f_ext}'
        os.rename(f, new_name)
