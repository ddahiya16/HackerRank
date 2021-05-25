def count_substring(string, sub_string):
    cnt = 0
    for i in range(0,len(string)):
        k = i
        m = 0
        for j in range(0, len(sub_string)):
            if((len(string)-i < len(sub_string)) or string[k] != sub_string[j]):
                break    
            k = k+1
            m = m+1
        if(m==len(sub_string)):
           cnt = cnt + 1         
    return cnt


if __name__ == '__main__':
