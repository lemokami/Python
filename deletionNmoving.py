import shutil as su

import os 

su.rmtree("dummy_folder/")

print("Making a dummy_folder for operations\n\n")
os.mkdir("dummy_folder")


print("Copying HelloWorld.py to dummy_folder and renaming as something.py")
direc = su.copy("HelloWorld.py","dummy_folder/something.py")
print(direc)


print("\n\nMoving something.py to the parent python folder and renaming it")
dec = input("Do you want to move it?[Y/N]:")
if(dec.upper() == 'Y'):
    print("Process Successful")
    print(su.move(direc,"../Python" ))



dec = input("\n\nDo you want to delete something.py?[Y/N]")
if(dec.upper() == 'Y'):
    try:
        os.unlink("../Python/something.py")
    except:
        os.unlink("dummy_folder/something.py")
print("--------Deleted something.py----------")



dec = input("\n\nDo you want to delete the dummy_folder?[Y/N]")
if(dec.upper() == 'Y'):
    su.rmtree("dummy_folder/")

print("\n\n----------Fin----------")

