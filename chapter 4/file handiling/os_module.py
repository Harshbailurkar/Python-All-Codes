import os
if(not os.path.exists("adata")):  #to check adata folder already exits or not(here we use not  #                                  in function to check if it is not exits then make adata #                                  folder)
   
    os.mkdir("adata")               # to creat a folder

# for i in range(0,10):
#     os.mkdir(f"adata/day{i+1}")     # to make a folder adata and in that make a subfolders day(1-10)


# to rename a folder

# for i in range(0,10):
#     os.rename(f"adata/day{i+1}", f"adata/tutorial {i+1}") 

# to know folders in file

folders=os.listdir("adata")

for folder in folders:
    print(folder)
    print(os.listdir(f"adata/{folder}"))

# to know in which directry you are

print(os.getcwd())

# to chenge the directory
