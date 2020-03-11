def perm(_str):
    __perm(_str, '')

def __perm(_str, prefix):
    if len(_str) == 0:
        print(prefix)
    else:
        for i in range(0, len(_str)):
            rem = _str[0:i] + _str[i+1:]
            __perm(rem, prefix + _str[i])


  
# Driver program to test the above function 
string = "ABC"
perm(string) 