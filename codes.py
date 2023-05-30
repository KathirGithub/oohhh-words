import time
import random
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEvent

from_dir='C:/users/paran/Downloads'

class FileEventHandler(FileSystemEvent):
    def on_created(self,event):
        print(f'Hi,{event.src_path} has been created')
    def on_deleted(self,event):
        print(f'Opps someone deleted, {event.src_path}')
    def on_modified(self,event):
        print(f'Hi there, {event.src_path} has been modified')
    def on_moved(self,event):
        print(f'Hallo someone moved,{event.src_path} to {event.dest_path}')

eventHandler=FileEventHandler
observer=Observer

observer.schedule(eventHandler,from_dir,recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print('running')
except KeyboardInterrupt:
    print('stop')
    observer.stop()