import threading
import os
import subprocess as sp
def errorCount():
    threading.Timer(5.0,errorCount).start()
    fname = ("/var/log/nginx/access.log")
    num1="200"
    num2="499"
    num3="500"
    count1= 0;
    count2= 0;
    count3= 0;
    sum=0;
    out1='ser1.conf'
    with open(fname, 'r') as f:
        for line in f:
            words1= line.split()
            for i in words1:
                if(i==num1):
                    count1=count1+1
    with open(fname, 'r') as f:
        for line in f:
            words2 = line.split()
            for i in words2:
                if(i==num2):
                    count2=count2+1
    with open(fname, 'r') as f:
        for line in f:
            words3 = line.split()
            for i in words3:
                if(i==num3):
                    count3=count3+1
    print("Occurrences of the number",num1,"is",count1)
    print("Occurrences of the number",num2,"is",count2)
    print("Occurrences of the number",num3,"is",count3)
    sum=count2+count3
    print("Total Erros:",sum)
    if(sum>=200):
        out = sp.getoutput('ls /etc/nginx/conf.d | grep ser1.conf')
        #print(out)
        b=(out1==out)
        #print(b)
        if(b==True):
            os.system('mv /etc/nginx/conf.d/ser1.conf /etc/nginx/conf.d/ser1.txt')
            os.system('mv /etc/nginx/conf.d/ser12.txt /etc/nginx/conf.d/ser12.conf')
            #os.system('mv /etc/nginx/conf.d/ser1.conf /etc/nginx/conf.d/ser1.txt')
            print("\n")
            os.system('service nginx reload')
            print("\n-----Server 2 Online-----\n")
        
errorCount()