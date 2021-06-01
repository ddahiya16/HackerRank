str = input()
count = 1
l = len(str)
if l == 1:
    t = (count, int(str[0]))
    print(t)
else:    
    for i in range(0,l-1):
        if i == 0 and str[i] != str[i+1]:
            t = (1, int(str[i]))
            print(t, end = " ")
            count = 1
        else:
            if str[i]== str[i+1]:
                count+=1
            else:
                t = (count, int(str[i]))
                print(t, end = " ")
                count = 1
                
        if(i==l-2):
            t = (count, int(str[i+1]))
            print(t)       
