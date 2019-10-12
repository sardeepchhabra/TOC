str=input("enter element consisting of 0 & 1 ")
n=len(str)
flag=0
for i in range(0,(n-2)):
    if(str[i]=='1' and str[i+1]=='1' and str[i+2]=='1'):
        flag=1
        break
if(flag!=0):
    print("yes")
else:
    print("No")
