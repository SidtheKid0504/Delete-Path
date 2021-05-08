import os
import time
import shutil

path = input("Enter File Path: ")

days = 30
sec = time.time() - (days * 24 * 60 * 60)

if os.path.exists(path):
    for root, dirs, files in os.walk(path, topdown = True):
        for n in files:
            path = os.path.join(root, n)
            _time = os.stat(path).st_ctime

            if sec >= _time:
                os.remove(path)
                print("Path Deleted")

        for n in dirs:
            path = os.path.join(root, n)
            _time = os.stat(path).st_ctime

            if sec >= _time:
                shutil.rmtree(path)
                print("Path Deleted")

else:
    print("Path Doesn't Exist")