import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from DataSaver import DataSaver

class CodeScapeEventHandler(FileSystemEventHandler):
    def __init__(self, file_list, file_types, path):
        super().__init__()
        self.data_saver: DataSaver = DataSaver(file_types, path)
        self.file_dict = {}
        for file in file_list:
            if file in self.file_dict:
                self.file_dict[file] = self.count_lines(file)
        self.line_changes = 0

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
        try:
            with open(filepath) as file:
                num_lines = len(file.readlines())
                file_name: str = str(os.path.basename(filepath))
                if file_name in self.file_dict:  # Check if key exists
                    self.line_changes += abs(self.file_dict[file_name] - num_lines)
                else:
                    self.line_changes += num_lines
                    self.file_dict[file_name] = num_lines
                xp: int = abs(self.file_dict[file_name] - num_lines)
                if xp >= 100:
                    print("+100xp")
                elif xp == 0:
                    print("+",str(1), "xp")
                else:
                    print("+", str(xp), "xp")

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