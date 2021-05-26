import threading

def errorCount():
    threading.Timer(5.0,errorCount).start()
    fname = ("log.txt")
    num1="200"
    num2="499"
    num3="500"
    count1= 0;
    count2= 0;
    count3= 0;
    sum=0;
    out1='abc.txt'
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
        out = os.popen('ls | grep abc.txt').read()
        print(out)
        b=(out1==out)
        print(b)
        if(b==True):
            os.system('mv abc.txt xyz.py')
            print("File successfully renamed")
errorCount()
