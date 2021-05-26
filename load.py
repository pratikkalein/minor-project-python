import os
import threading

def load():
    threading.Timer(5.0,load).start()
    os.system('ab -n 5000 -c 1000 http://example.minor/')
    print("\nLoading nginx....\n")
           
load() #calling load function

