import os
import zipfile

# get the path to the user's AppData/Roaming folder
appdata_path = os.getenv('APPDATA')

# create the path to the .minecraft folder
minecraft_path = os.path.join(appdata_path, '.minecraft')

# create the path to the mods folder inside .minecraft
mods_path = os.path.join(minecraft_path, 'mods')

# make sure the mods folder exists
if os.path.exists(mods_path):
    print(f"Successfully found dir {mods_path}")
else:
    print(f"No directory found. Please install 1.18.2 fabric client")
    input()
    exit()

# specify the path and name of the zip file
zip_path = './mods.zip'
print("mods.zip found")

# create a ZipFile object with the specified path
zip_file = zipfile.ZipFile(zip_path)

# extract all the contents of the zip file to the mods folder
zip_file.extractall(mods_path)
print(f"Extracted file(s) to {mods_path}")

# close the ZipFile object
zip_file.close()
input("Successfully unzipped files")
