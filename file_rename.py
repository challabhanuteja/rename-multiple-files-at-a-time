import os
os.chdir('E:\Web Development Tutorials') #going to directory
a = os.listdir() # a is the list of all files in the current working directory
for i in a: #iterating through all the file names in a
    # this code changes according to your need
    if(' #' in i):
        j = i.replace(".mp4","")
        j = j.split(" #")
        s = j[1]+". "+j[0]+".mp4"
        # print(i,s)
        os.rename(i,s) # i is present name of the file, s is the new file name.