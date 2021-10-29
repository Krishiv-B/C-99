import os
import shutil
def sortAndSwapFileData():
    path=input("Enter the directory that you want to sort from:")
    
    listOfFiles=os.listdir(path)
    for file in listOfFiles:
        name,ext=os.path.splitext(file)
        ext=ext[1:]
        if ext=="":
            continue
        if os.path.exists(path+"/"+ext):
            shutil.move(path+"/"+file, path+"/"+ext+"/"+file)
        else:
            os.makedirs(path+"/"+ext)
            shutil.move(path+"/"+file, path+"/"+ext+"/"+file)

    
    
sortAndSwapFileData()  