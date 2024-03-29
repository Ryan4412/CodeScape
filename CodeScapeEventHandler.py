import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from DataSaver import DataSaver
import random

class CodeScapeEventHandler(FileSystemEventHandler):
    def __init__(self, file_list: list, file_list_with_path: list, file_types: dict, path: str, extention_list: list):
        super().__init__()
        self.data_saver: DataSaver = DataSaver(file_types, path)
        self.extention_list: list = extention_list
        self.file_list_with_path: list = file_list_with_path
        self.file_dict = {}
        for file in file_list:
            # if file in self.file_dict:
            for file_path in file_list_with_path:
                file_name: str = file_path
                file_name: str = str(os.path.basename(file_name))
                if file_name == file:
                    print(f"compairing {file} and {file_name}")
                    print(f"with path {file_path}")
                    self.file_dict[file] = self.count_lines(file_path)
                # self.file_dict[file] = self.count_lines(file)
        self.line_changes = 0
        print(self.file_dict)

    def count_lines(self, file):
        try:
            with open(file, 'r') as file:
                return len(file.readlines())
        except FileNotFoundError:
            print("File was not found durrent line_count")

    def on_modified(self, event):
        if event.is_directory:
            return
        print(f"File {event.src_path} has been modified")
        self.count_line_changes(event.src_path)

    def count_line_changes(self, filepath):
        print("file path -> ",filepath)
        try:
            with open(filepath) as file:
                num_lines = len(file.readlines())
                file_name: str = str(os.path.basename(filepath))
                if file_name in self.file_dict:  # Check if key exists
                    print("self.file_dict[file_name] -> ", self.file_dict[file_name])
                    print("num_lines -> ", num_lines)
                    self.line_changes += abs(self.file_dict[file_name] - num_lines)
                else:
                    self.line_changes += num_lines
                    self.file_dict[file_name] = num_lines
                lines_changed: int = abs(self.file_dict[file_name] - num_lines)
                extention: str = file_name.split('.')[1]
                self.data_saver.addXPtoLanguageForFileModification(extention, lines_changed)
                self.file_dict[file_name] = num_lines
        except FileNotFoundError:
            pass

    def on_created(self, event):
        if event.is_directory:
            return
        print(f"File {event.src_path} has been created")
        self.count_line_changes(event.src_path)

    def on_deleted(self, event):
        if event.is_directory:
            return
        print(f"File {event.src_path} has been deleted")

    def game_tick(self):
        random_index: int = random.randint(0, len(self.extention_list) - 1)
        self.data_saver.addXpToLanguageForGameTick(self.extention_list[random_index])
        print(f"+ 5 {self.extention_list[random_index]} xp")

