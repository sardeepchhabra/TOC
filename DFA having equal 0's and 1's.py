In [3]:
dfa = {
    'a':{0:'b',1:'b'},
    'b':{0:'a',1:'a'}
}

def func4(r):
    s = str(r)
    ins = 'a'
    fis = ['a']
    for i in s:
        ins = dfa[ins][int(i)]
    if ins in fis:
        return True
    else:
        return False

func4('11000011')
Out[3]:
True