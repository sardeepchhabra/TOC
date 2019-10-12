stack=['z0']
str1=input()
a=0
for i in str1:
    if i=='a' and a==0:
        stack.append(i)
    elif i=='b':
        stack.pop()
        a=1
if len(stack)>0 and stack[-1]=='z0':
    print('accepted')
else:
    print('not accepted')
