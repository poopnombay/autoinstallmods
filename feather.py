import os
import zipfile

# get the path to the user's AppData/Roaming folder
appdata_path = os.getenv('APPDATA')

# create the path to the .feather folder
feather_path = os.path.join(appdata_path, '.feather')

# create the path to the mods folder inside .feather
user_mods_path = os.path.join(feather_path, 'user-mods')

# find fabric mod path
fabric_mods_path = os.path.join(user_mods_path, '1.18.2-fabric')

# make sure the mods folder exists
if os.path.exists(fabric_mods_path):
    print(f"Successfully found dir {fabric_mods_path}")
else:
    print(f"No directory \'{fabric_mods_path}\'found. Please install minecraft version 1.18.2 in feather client")
    input()
    exit()

# specify the path and name of the zip file
zip_path = './mods.zip'
print("mods.zip found")

# create a ZipFile object with the specified path
zip_file = zipfile.ZipFile(zip_path)

# extract all the contents of the zip file to the mods folder
zip_file.extractall(fabric_mods_path)
print(f"Extracted file(s) to {fabric_mods_path}")

# close the ZipFile object
input(f"Successfully unzipped files to {fabric_mods_path}")
zip_file.close()
