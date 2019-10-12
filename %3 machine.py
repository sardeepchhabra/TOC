  
def start( c):  
   
    if (c == 'a'):   
        dfa = 10 
       
    elif (c == 'b') :  
        dfa = 1 
       
    
     #-1 is used to check for any invalid symbol  
    else:   
        dfa = -1
    return dfa 
       
   
    
# This function is for the first state (01) of DFA  
def state01( c):  
   
    if (c == 'a'):   
        dfa = 11 
       
    elif (c == 'b') :  
        dfa = 2 
       
    else:   
        dfa = -1
    return dfa 
   
    
# This function is for the second state (02) of DFA  
def state02( c):  
   
    if (c == 'b') :  
        dfa = 0 
       
    elif(c =='a'): 
      
        dfa = 12
      
    else:   
        dfa = -1
    return dfa 
       
   
    
# This function is for the third state (10)of DFA  
def state10( c):  
   
    if (c == 'b') :  
        dfa = 11 
       
    elif(c =='a'): 
      
        dfa = 20
      
    else:   
        dfa = -1
    return dfa 
       
   
  
# This function is for the forth state (11)of DFA  
def state11( c):  
   
    if (c == 'b') :  
        dfa = 12 
       
    elif(c =='a'): 
      
        dfa = 21
      
    else:   
        dfa = -1
    return dfa 
       
   
  
def state12( c):  
   
    if (c == 'b') :  
        dfa = 10 
       
    elif(c =='a'): 
      
        dfa = 22
      
    else:   
        dfa = -1
    return dfa 
       
   
  
def state20( c):  
   
    if (c == 'b') :  
        dfa = 21 
       
    elif(c =='a'): 
      
        dfa = 0
      
    else:   
        dfa = -1
    return dfa 
       
  
  
def state21( c):  
   
    if (c == 'b') :  
        dfa = 22 
       
    elif(c =='a'): 
      
        dfa = 1
      
    else:   
        dfa = -1
    return dfa 
  
  
def state22( c):  
   
    if (c == 'b') :  
        dfa = 20 
       
    elif(c =='a'): 
      
        dfa = 2
      
    else:   
        dfa = -1
    return dfa 
       
  
  
def isAccepted(str):  
   
    # store length of string  
    l = len(str) 
    # dfa tells the number associated   
    # with the present dfa = state   
    dfa = 0
      
    for i in range(l):   
        if (dfa == 0) : 
            start(str[i])  
    
        elif (dfa == 1):  
            state01(str[i])  
    
        elif (dfa == 2) : 
            state02(str[i])  
    
        elif (dfa == 10) : 
            state10(str[i])  
    
        elif (dfa == 11) : 
            state11(str[i])  
              
        elif (dfa == 12) : 
            state12(str[i])  
          
        elif (dfa == 20) : 
            state20(str[i])  
    
        elif (dfa == 21) : 
            state21(str[i])  
    
        elif (dfa == 22) : 
            state22(str[i])  
              
        else: 
            return 0 
       
    if (dfa == 0 or dfa == 11 or dfa == 22) : 
        return 1 
    else: 
        return 0 
   
    
# Driver code    
if __name__ == "__main__" :  
   
    string = "aaaabbbb" 
    if (isAccepted(string)) : 
        print("ACCEPTED")  
    else: 
        print("NOT ACCEPTED")  
   
