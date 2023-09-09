R = open('file.txt','r')  # first is file name and second one is for mode to be open
                          # r- read, w- write, a- appending(adding additional content in file)
                          # r mode is defalut mode
text=R.read()
print(text)
R.close()

# rt -read text file(default)
#rb - read binary content [ use to read jpg img pdf file]

# writing to a file

W=open('file.txt','w')
W.write("hello harsh!!!!!!!!")
W.close()

#append to a file
W=open('file.txt','a')
W.write("hello harsh!!!!!!!!")
W.close()


# to avoid close() use with

with open('file.txt','a') as a:
    a.write("hey i am inside")