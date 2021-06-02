from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import time

if __name__ == "__main__":
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

def on_creation(event):
    if(f"{event.src_path}" != f"./log.txt"):
        with open("log.txt", "a") as file:
                file.write(f"{event.src_path} created!\n")

def on_deletion(event):
    if(f"{event.src_path}" != f"./log.txt"):
        with open("log.txt", "a") as file:
            file.write(f"{event.src_path} deleted!\n")

def on_modification(event):
    if(f"{event.src_path}" != f"./log.txt"):
        with open("log.txt", "a") as file:
            file.write(f"{event.src_path} modified!\n")


my_event_handler.on_created = on_creation
my_event_handler.on_deleted = on_deletion
my_event_handler.on_modified = on_modification

path = "."
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=True)

my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
