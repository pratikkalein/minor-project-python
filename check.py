import threading
import os
import subprocess as sp
def errorCount():
    threading.Timer(5.0,errorCount).start()
    a=300
    out1='abc.txt'
    if(a>=200):
        out = sp.getoutput('ls | grep abc.txt')
        print(out)
        b=(out1==out)
        print(b)
        if(b==True):          
            os.system('mv abc.txt xyz.py')
            #os.system('service nginx reload')
            print("File successfully renamed")	
errorCount()
