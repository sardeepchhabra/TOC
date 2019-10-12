n=input()
count1=0
count2=0
for i in n:
    if(i=='a'):
        count1+=1
    else:
        break;
for i in n[count1:]:
    if(i=='a'):
        
        break

if(count1%2==0 and i=='b'):
    print("Accepted")
else:
    print("not accepted")
