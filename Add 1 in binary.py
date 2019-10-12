def inc(binary):
    lst_binary = list(binary)
    for bit in range(len(binary)-1, -1, -1):
        if lst_binary[bit] == '0':
            lst_binary[bit] = '1'
            return ''.join(lst_binary)
        else:
            lst_binary[bit] = '0'
			lst_binary.insert(0,'1')
    return ''.join(lst_binary)
