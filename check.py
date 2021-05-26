import threading
import os

def errorCount():
    threading.Timer(5.0,errorCount).start()
    a=300
    out1='abc.txt'
    if(a>=200):
        out = os.popen('ls | grep abc.txt').read()
        print(out)
        b=(out1==out)
        print(b)
        if(b==True):          
            os.system('mv abc.txt xyz.py')
            os.system('service nginx reload')
            print("File successfully renamed")	
errorCount()
