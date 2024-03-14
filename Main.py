import os 
import time
from Session import Session

print("Please enter the directory you will be programming in today:")
path: str = input() # user enters directory they will be editing in 
print("Python read yout current working directory as: " + path)
file_list: list = os.listdir(path) # stores the list of files in the directory
file_types: list = []
for file in file_list:

    file_path: str = f'{path}\\{file}' # parses an individual file path
    type: str = str(file)
    if os.path.isfile(file_path):
        try:
            print(file)
            getType: list = type.split('.')
            if not file_types.__contains__(getType[1]):
                file_types.append(getType[1])
        except:
            print(f'ALERT: {file} could not be printed!')
    else:
        print(f'ALERT: {file} is not a file, so it can not be printed!')

print(f'your files types are: {file_types}')

newSession: Session = Session(file_types)

while(True):
    time.sleep(5)
    newSession.run()
