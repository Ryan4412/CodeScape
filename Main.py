import os 
import time
from DataSaver import DataSaver
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from CodeScapeEventHandler import CodeScapeEventHandler
from pathlib import Path

# recursivly walks through a directory and adds all the files in the path specified to the list
def list_files(directory) -> list:
    valid_file_types: dict = {
        'py' : 0, 'js' : 0, 'java' : 0, 
        'cs' : 0, 'php' : 0, 'cpp' : 0,
        'c' : 0, 'r' : 0, 'swift' : 0,
        'kt' : 0, 'json' : 0, 'ts' : 0,
        'go' : 0, 'rs' : 0, 'jsx' : 0,
        'html' : 0, 'css' : 0, 'sh' : 0,
        'lua' : 0, 'zig' : 0, 'ml' : 0,
    }

    file_list: list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            # print(os.path.join(root, file))
            # s = os.path.join(root, file)
            # print(s)
            # print(file)
            file_name: str = str(file)
            try:
                if file_name.split('.')[1] in valid_file_types:
                    file_list.append(file_name)
            except IndexError:
                print(f"({file}) is not a valid Not a file")

    return file_list


# recursivly walks through a directory and adds all the files in the path specified to the list
def listFilesWithPath(directory) -> list:

    file_list_with_path: list[Path] = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            # print(os.path.join(root, file))
            # print(Path(os.path.join(root, file)))
            file_list_with_path.append(Path(os.path.join(root, file)))

    print(file_list_with_path)
    
    return file_list_with_path

def getFileTypes(file_list) -> dict:
    file_types: dict = {
        'py' : 0, 'js' : 0, 'java' : 0, 
        'cs' : 0, 'php' : 0, 'cpp' : 0,
        'c' : 0, 'r' : 0, 'swift' : 0,
        'kt' : 0, 'json' : 0, 'ts' : 0,
        'go' : 0, 'rs' : 0, 'jsx' : 0,
        'html' : 0, 'css' : 0, 'sh' : 0,
        'lua' : 0, 'zig' : 0, 'ml' : 0,
    }
    for file in file_list:
        # print(file, " grabs: ", str(file).split('.')[1])
        try:
            extention: str = str(file).split('.')[1] # ex: will grab c in main.c
            if extention in file_types:
                file_types[extention] += 1
        except IndexError:
            print(f"({file}) is not a valid Not a file")
        
    
    return file_types

def getExtentionList(file_list) -> list:
    extention_list: list = []
    for file in file_list:
        try: 
            extention_list.append(str(file).split('.')[1])
        except IndexError:
            print(f"({file}) is not a valid Not a file")
    
    return extention_list





print("Please enter the directory you will be programming in today:")
path: str = input() # user enters directory they will be editing in 
if not os.path.isdir(path):
        print("Invalid directory path.")
        exit()
# file_list: list = os.listdir(path) # stores the list of files in the directory
file_list: list = list_files(path)
file_list_with_path: list[Path] = listFilesWithPath(path)
print(file_list_with_path)
file_types: dict = getFileTypes(file_list)
extention_list: list = getExtentionList(file_list)

event_handler = CodeScapeEventHandler(file_list, file_list_with_path, file_types, path, extention_list)
observer = Observer()
observer.schedule(event_handler, path=path, recursive=True)
observer.start()

try:
    while(True):
        time.sleep(5)
        event_handler.game_tick()
except KeyboardInterrupt:
    print(f"Total line changes this session: {event_handler.line_changes}")
    observer.stop()

observer.join()
