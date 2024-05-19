import sys
import time
import logging
from os import scandir
from shutil import move
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source_dir = 'C:/Users/samue/Downloads'
dest_model_dir = 'C:/Users/samue/OneDrive/3D Models'

model_extensons = (".stl", ".3mf", ".STL", "3MF")



class MoveHandler(FileSystemEventHandler):
    
    def on_modified(self,event):
        with scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                if name.endswith(model_extensons):
                    move(entry, dest_model_dir)
                    print(name)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    logging.info(f'start watching directory {path!r}')
    event_handler = MoveHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()