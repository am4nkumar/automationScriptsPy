import sys
import clipboard
import json
import os
from termcolor import colored

DEFAULT_FILE = "clipboard.json"
CONFIG_FILE = "conf.json"

def saveConfig(key, pathVal):
    confData = load_data(CONFIG_FILE)
    confData[key] = pathVal
    print(confData)
    save_data(CONFIG_FILE,confData)
    print(colored(f"Config file updated successfully. updated entry:  {key} = {pathVal}", "green"))

def createFile():
    pathF = input(r"Enter the path of the file: ")
    nameF = input(r"Enter the name of the file: ")
    fullPath = pathF+nameF+".json"
    open(fullPath, "x")
    print(colored(f"File {nameF} was created successfully, fullpath => {fullPath}", "green"))
    saveConfig(nameF,fullPath)

def fileSelector(fileName):
    with open(CONFIG_FILE,"r") as f:
        config_data = json.load(f)
        if fileName in config_data:
            SAVED_DATA = config_data[fileName]
            return SAVED_DATA

def checkoutConf():
    dataRaw = load_data(CONFIG_FILE)
    listT = [(k, v) for k, v in dataRaw.items()]
    newdir = {}

    for x in listT:
        path = x[1]
        fname, fpath = str(x[0]), str(x[1])
        if(os.path.isfile(path)):
            newdir[fname] = fpath
    save_data(CONFIG_FILE, newdir)

def listFile(fileName):
    data = load_data(CONFIG_FILE)
    if fileName in data:
        fileData = load_data(data[fileName])
        for i in fileData:
            print(f"{i} : {fileData[i]}")

def listconfig():
    data = load_data(CONFIG_FILE)
    for i in data:
        print(f"{i} : {data[i]}")

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return{}

def checkSuite( SAVED_DATA):
    if command == "save":
        key = input("Enter a key:")
        data = load_data(SAVED_DATA)
        data[key] = clipboard.paste()
        save_data(SAVED_DATA,data)
        print(colored("Data saved to the file successfully","green"))

    elif command == "load":
        key = input("Enter a key:")
        data = load_data(SAVED_DATA)
        if key in data:
            clipboard.copy(data[key])
            print(colored("Data copied to the clipboard","green"))
        else:
            print(colored("Key does not exist."),"red")

    elif command == "list":
        choice = input("Enter the name of the file to be listed : ")
        listFile(choice)

    elif command == "listconf":
        listconfig()

    elif command == "create":
        createFile()

    elif command == "checkout":
        checkoutConf()

    else:
        print("Unknown command")

if len(sys.argv) == 3:
    command = sys.argv[2]
    fileselected = sys.argv[1]
    checkSuite((fileSelector(fileselected)))
elif len(sys.argv) == 2:
    command = sys.argv[1]
    checkSuite(DEFAULT_FILE)
else:
    print(colored("Error: Please pass the commands properly", "red"))
    print("Proper Usage => \n 1. python multi_clipboard.py create\n 2. python multi_clipboard.py FILENAME {save/load/list}\n 3. python multi_clipboard.py {save/load/list}   # This will work on clipboad.json file only" )