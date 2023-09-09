# seek()
with open("file.txt","r") as f:
    print(type(f))

    f.seek(10)   # move to the 10th byte in the file
    data=f.read(5) # read the next 5 byte in file (reading start after 10 char)
    print(data)
    print(f.tell()) # return the current position
    

with open("file.txt","w") as w:
     w.write("harsh bailurkar")
     w.truncate(5)

with open("file.txt","r") as a:
    let=a.read()
    print(let)

