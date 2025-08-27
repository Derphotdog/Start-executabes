from subprocess import Popen as start
from os import path as os_path

script_dir = os_path.dirname(os_path.realpath(__file__))
PathLocation = os_path.join(script_dir, "Start_Executables_Paths.txt")

if os_path.isfile(PathLocation) == False:
    open("Start_Executables_Paths.txt", "x")

update = input("Do you want to add any paths?(Programs to run) y or n?: ").upper()

if update=="Y":
    
    with open(PathLocation, "a") as PathFile:
        if os_path.getsize(PathLocation) == 0:
            PathFile.write(f"{input("Enter full path: ").replace("\\", "\\\\").strip('"')}")
        else:
            PathFile.write(f",{input("Enter full path: ").replace("\\", "\\\\").strip('"')}")
else:
    OpenList = open(PathLocation, "r").read().split(",")
    for x in range(len(OpenList)):
        path = OpenList[x]
        if os_path.isfile(path):
            if "obs64.exe" in path:
                start([path],cwd='C:\\Program Files\\obs-studio\\bin\\64bit\\')
            else:
                start([path])
        else:
            if path!="":
                print(f"ERROR, File not found: {path}")
            else:
                print("ERROR, No Paths Found")