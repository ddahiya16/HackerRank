def swap_case(s):
    l = ""
    for i in s:
        if(i.islower()):
            l = l+i.upper()
        else:
            l = l+i.lower()       
    return l

if __name__ == '__main__':
