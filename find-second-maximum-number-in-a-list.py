if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())

arr.sort(reverse = True)
temp = 0
for i in arr:
    if temp!= 0 and temp>i:
        print(i)
        break
    temp = i
