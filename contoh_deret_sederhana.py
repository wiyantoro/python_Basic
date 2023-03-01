import time
 
start=1
fininsh=5
nilaike=0
while(start<=fininsh):
    #print(start)
    if start==1:
        print(start)
        nilaike=start
    if start>=2:
        nilaike=(nilaike*2)+1
        print(nilaike)
    time.sleep(1)
    start+=1