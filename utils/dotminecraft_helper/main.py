### main command
command="switch 1.21->1.21.11 true true"
#command="compare 1.21.11 26.2 true"
#command="transferto 26.2"
#command="transferfrom 26.2 true"

dirs={"1.21.11":"ВСЕГДА 1.21.11","26.2":"ВСЕГДА 26.2","1.21":"ВСЕГДА версии\\1.21"} #do not use spaces or arrows (->, <-) in index name
transfer_whitelist=[".txt",".zip",".rar",".jar",".disabled",".json"]

#switch [indexInDirsOld || indexInDirsNew: str][-> || <-][indexInDirsNew || indexInDirsOld: str] [saveOptions: bool] [loadOptions: bool]
# transfers files from "mods" folder to [indexInDirsOld], after that transfers files from [indexInDirsNew] to "mods" folder.
# can be given 2 additional arguments:
#  the first one will allow to save "options.txt" into [DirsOld] folder,
#  the second one will load "options.txt" from "mods" folder into the minecraft root (after transferring mods from [DirsNew] to "mods")

#compare [indexInDirs1: str] [indexInDirs2: str] [useModid (true): bool]
# Compares mod names in 2 given folders [indexInDirs1] and [indexInDirs2], outputs a list of missing mods in every folder relating to the other one
# By default it uses mods' "modid"s for searching, but it might take some time on old computers. The main advantage of this method - clear names:
# idc_about_the_filename----1.1.1.1.1_some_mod_with_towers--26.2.jar -> name: The Tower Mod, modid: tower_mod
# If you set useModid value on false, then the script will only use filenames to compare (trims the filename right before any digits start)
# This method is fast, but sometimes inaccurate
# some_mod_v1.1.1.1-26.2alpha.jar -> some_mod
# idc_about_the_filename----1.1.1.1.1_some_mod_with_towers--26.2.jar -> idc_about_the_filename--

#transferto [dir: str] [saveOptions: bool]
# transfers files from "mods" folder to [dir] folder

#transferfrom [dir: str] [loadOptions: bool]
# transfers files from [dir] folder to "mods" folder



import os
import shutil
import logging
import re
import zipfile
import tomllib
import json

dotminecraft=os.getenv("APPDATA")+"\\.minecraft\\"
logger=logging.getLogger(__name__)

def logger_setup():
    global logger
    logger.setLevel(logging.ERROR)
    formatter = logging.Formatter('[%(levelname)s] [%(asctime)s] %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    with open("latest.log", "w", encoding="utf-8") as f: f.write("")
    file_handler = logging.FileHandler("latest.log", mode="a", encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
logger_setup()

def bool_str(string: str) -> bool:
    if string=="true" or string=="True" or string=="TRUE" or string=="1b" or string=="1":
        return True
    elif string=="false" or string=="False" or string=="FALSE" or string=="0b" or string=="0":
        return False
    else:
        raise Exception("boolean values should look like 'true' or 'True' or 'TRUE' or '1b' or '1' and nothing else!")

def switch(dirs: dict, old: str, new: str):
    global dotminecraft, transfer_whitelist
    dirold=dotminecraft+"mods\\"+dirs[old]
    dirnew=dotminecraft+"mods\\"+dirs[new]
    #print(dirold)
    #print("mods:",os.listdir(dirold),"\nExtension step 1:",os.path.splitext(dirold+"\\"+os.listdir(dirold)[0]),"\nExtension step 2:",os.path.splitext(dirold+"\\"+os.listdir(dirold)[0])[1])
    mods_in_root=[mod for mod in os.listdir(dotminecraft+"mods") if os.path.splitext(dotminecraft+"mods\\"+mod)[1] in transfer_whitelist]
    mods_to_transfer=[mod for mod in os.listdir(dirnew) if os.path.splitext(dirnew+"\\"+mod)[1] in transfer_whitelist]
    #print(mods_in_root)
    logger.info("STARTING TRANSFER TO OLD")
    for mod in mods_in_root:
        shutil.move(dotminecraft+"mods\\"+mod, dirold+"\\")
        logger.debug(f"transfered {mod}")
        #print(dotminecraft+"mods\\"+mod,dirold+"\\",sep="\t\t")
    logger.info("STARTING TRANSFER FROM NEW")
    for mod in mods_to_transfer:
        shutil.move(dirnew+"\\"+mod, dotminecraft+"mods\\")
        logger.debug(f"transfered {mod}")

def load_options():
    global dotminecraft
    shutil.copy(dotminecraft+"mods\\options.txt",dotminecraft+"\\options.txt")

def save_options(old_mod_dir: str):
    global dotminecraft
    shutil.copy(dotminecraft+"\\options.txt",dotminecraft+"mods\\"+old_mod_dir+"\\options.txt")

def trim_mod(mod: str) -> str:
    return re.sub(r"\d.*$", "", mod).rstrip("-").rstrip("_").rstrip("-")

def get_modid(path: str, mod: str) -> tuple[str,str]:
    if os.path.splitext(mod)[1]!=".jar" and os.path.splitext(mod)[1]!=".disabled":
        t=trim_mod(mod)
        return t,t
    with zipfile.ZipFile(path+"\\"+mod, "r") as zf:
        files=zf.namelist()
        mods_forge="META-INF/mods.toml"
        mods_neoforge="META-INF/neoforge.mods.toml"
        mods_quilt="quilt.mod.json"
        mods_fabric="fabric.mod.json"

        if mods_forge in files:
            with zf.open(mods_forge) as tomlf:
                data_bytes=tomlf.read()
                data=tomllib.loads(data_bytes.decode('utf-8'))
                modid=data["mods"][0]["modId"]
                name=data["mods"][0]["displayName"]
        elif mods_neoforge in files:
            with zf.open(mods_neoforge) as tomlf:
                data_bytes=tomlf.read()
                data=tomllib.loads(data_bytes.decode('utf-8'))
                modid=data["mods"][0]["modId"]
                name=data["mods"][0]["displayName"]
        elif mods_quilt in files:
            with zf.open(mods_quilt) as jsonf:
                data_bytes=jsonf.read()
                data=json.loads(data_bytes.decode('utf-8').replace("\n"," "))
                modid=data["quilt_loader"]["id"]
                name=data["quilt_loader"]["metadata"]["name"]
        elif mods_fabric in files:
            with zf.open(mods_fabric) as jsonf:
                data_bytes=jsonf.read()
                data=json.loads(data_bytes.decode('utf-8').replace("\n"," "))
                modid=data["id"]
                name=data["name"]
        else:
            modid=trim_mod(mod)
            name=modid

    return str(modid),str(name)

def compare(dirs: dict, dir1: str, dir2: str, use_modid=True):
    global dotminecraft
    #fp - full path
    dir1_fp=dotminecraft+"mods\\"+dirs[dir1]
    dir2_fp=dotminecraft+"mods\\"+dirs[dir2]
    dir1_mods=[mod for mod in os.listdir(dir1_fp) if os.path.splitext(dir1_fp+"\\"+mod)[1] in transfer_whitelist]
    dir2_mods=[mod for mod in os.listdir(dir2_fp) if os.path.splitext(dir2_fp+"\\"+mod)[1] in transfer_whitelist]
    if not use_modid:
        dir1_mods=[trim_mod(mod) for mod in dir1_mods]
        dir2_mods=[trim_mod(mod) for mod in dir2_mods]
        print(f"MISSING IN {dir2}:")
        for mod in dir1_mods:
            if mod not in dir2_mods: print("    ",mod)
        print(f"MISSING IN {dir1}:")
        for mod in dir2_mods:
            if mod not in dir1_mods: print("    ",mod)
    else:
        dir1_mods=[get_modid(dir1_fp,mod) for mod in dir1_mods]
        dir2_mods=[get_modid(dir2_fp,mod) for mod in dir2_mods]
        dir1_mods={mod[0]:mod[1] for mod in dir1_mods}
        dir2_mods={mod[0]:mod[1] for mod in dir2_mods}
        print(f"MISSING IN {dir2}:")
        for modid in dir1_mods:
            if modid not in dir2_mods: print(f"    {dir1_mods[modid]} ({modid})")
        print(f"MISSING IN {dir1}:")
        for modid in dir2_mods:
            if modid not in dir1_mods: print(f"    {dir2_mods[modid]} ({modid})")


def transferto(dirs: dict, to_dir: str):
    global dotminecraft
    to_dir=dotminecraft+"mods\\"+dirs[to_dir]
    mods=[mod for mod in os.listdir(dotminecraft+"mods\\") if os.path.splitext(dotminecraft+"mods\\"+mod)[1] in transfer_whitelist]
    for mod in mods:
        shutil.move(dotminecraft+"mods\\"+mod, to_dir)

def transferfrom(dirs: dict, from_dir: str):
    global dotminecraft
    from_dir=dotminecraft+"mods\\"+dirs[from_dir]
    mods=[mod for mod in os.listdir(from_dir+"\\") if os.path.splitext(from_dir+"\\"+mod)[1] in transfer_whitelist]
    for mod in mods:
        shutil.move(from_dir+"\\"+mod,dotminecraft+"mods\\")

command=command.split(" ")
if command[0]=="switch":
    if command[1].find("->")!=-1:
        old, new = command[1].split("->")
    elif command[1].find("<-")!=-1:
        new, old = command[1].split("<-")
    switch(dirs, old, new)
    if len(command)>=3 and bool_str(command[2]):
        try: save_options(dirs[old])
        except FileNotFoundError:
            logger.error("Unable to transfer 'options.txt' to mods file, because it doesn't exist in root folder")
    if len(command)>=4 and bool_str(command[3]):
        try: load_options()
        except FileNotFoundError:
            logger.error("Unable to transfer 'options.txt' from mods file, because it doesn't exist there")
elif command[0]=="compare":
    if len(command)>=4:
        compare(dirs,command[1],command[2],bool_str(command[3]))
    if len(command)==3:
        compare(dirs,command[1],command[2])
elif command[0]=="transferto":
    transferto(dirs, command[1])
    if len(command)>=3 and bool_str(command[2]):
        load_options()
elif command[0]=="transferfrom":
    transferfrom(dirs, command[1])
