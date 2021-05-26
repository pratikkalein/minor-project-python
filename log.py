import threading

def errorCount():
    threading.Timer(5.0,errorCount).start()
    fname = ("/var/log/nginx/access.log")
    num1="200"
    num2="499"
    num3="500"
    count1= 0;
    count2= 0;
    count3= 0;

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
    print("Total Erros:",count2+count3)

errorCount()
