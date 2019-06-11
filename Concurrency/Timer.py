import os
import threading


def  exec_watcher():
    timer = threading.Timer(5.0, hello)
    timer.start()

def print_files():
    for i in os.listidr('.'):
        print(i)
    exec_watcher()


print_files()