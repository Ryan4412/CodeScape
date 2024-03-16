import os 
import time
from DataSaver import DataSaver
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# recursivly walks through a directory and adds all the files in the path specified to the list
def list_files(directory) -> list:
    file_list: list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            # print(os.path.join(root, file))
            # print(file)
            file_name: str = str(file)
            file_list.append(file_name)
    
    return file_list

def getFileTypes(file_list) -> dict:
    file_types: dict = {
        'py' : 0, 'js' : 0, 'java' : 0, 
        'py' : 0, 'py' : 0, 'py' : 0,
        'py' : 0, 'py' : 0, 'py' : 0,
        'py' : 0, 'py' : 0, 'py' : 0,
        'py' : 0, 'py' : 0, 'py' : 0,
        'py' : 0, 'py' : 0, 'py' : 0,
        'py' : 0, 'py' : 0, 'py' : 0,
    }
    for file in file_list:
        file_extention: str = str(file).split('.')[1] # ex: will grab c in main.c
    
    return file_types



print("Please enter the directory you will be programming in today:")
path: str = input() # user enters directory they will be editing in 
print("Python read yout current working directory as: " + path)
# file_list: list = os.listdir(path) # stores the list of files in the directory

file_list: list = list_files(path)
file_types: dict = {}

print(f'your files types are: {file_types}')

newSession: DataSaver = DataSaver(file_types, path)

while(True):
    time.sleep(5)
    newSession.run()