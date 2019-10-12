In [37]:
dfa = {
    'a':{0:'a',1:'b'},
    'b':{0:'c',1:'b'},
    'c':{0:'a',1:'d'},
    'd':{0:'a',1:'a'},
    'e':{0:'e',1:'e'},
    
}

def myfunc2(r):
    s = str(r)
    ins = 'a'
    fis = ['d']
    for i in s:
        ins = dfa[ins][int(i)]
    if ins in fis:
        return True
    else:
        return False

myfunc2('01011111100101011011101')
Out[37]:
True