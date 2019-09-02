import shutil as su #shutil helps to edit and manipulate files

import os #os module to change directory and stuff

su.rmtree("dummy_folder/") #.rmtree -> removes the folder specified if any
#su.rmtree("dummy_folder\\") -> comment the above statement and use this for windows

print("Making a dummy_folder for operations\n\n")
os.mkdir("dummy_folder") #.mkdir makes a directory or folder


print("Copying HelloWorld.py to dummy_folder and renaming as something.py")
direc = su.copy("HelloWorld.py","dummy_folder/something.py")#takes the HelloWorld.py files and copies it to the dummy folder and changes its name
#direc = su.copy("HelloWorld.py","dummy_folder\\something.py") -> comment the above statement and use this for windows
print(direc)


print("\n\nMoving something.py to the parent python folder and renaming it")
dec = input("Do you want to move it?[Y/N]:")
if(dec.upper() == 'Y'):
    print("Process Successful")
    print(su.move(direc,"../Python" ))
    #print(su.move(direc,"..\\Python" )) -> comment the above statement and use this for windows



dec = input("\n\nDo you want to delete something.py?[Y/N]")
if(dec.upper() == 'Y'):
    try:
        os.unlink("../Python/something.py") #.unlink removes the file 
        #os.unlink("..\\Python\\something.py") -> comment the above statement and use this for windows
    except:
        os.unlink("dummy_folder/something.py")
        #os.unlink("dummy_folder\\something.py") -> comment the above statement and use this for windows
print("--------Deleted something.py----------")



dec = input("\n\nDo you want to delete the dummy_folder?[Y/N]")
if(dec.upper() == 'Y'):
    su.rmtree("dummy_folder/")#removes the folder if the decision is made
    #su.rmtree("dummy_folder\\") -> comment the above statement and use this for windows

print("\n\n----------Fin----------")

