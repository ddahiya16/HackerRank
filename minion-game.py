def minion_game(string):
    s = string
    SC = []
    KV = []
    l = len(s)
    sScore = 0
    kScore = 0
    for i in range(0,l):
        if s[i] in ("A","E", "I", "O", "U"):
             kScore += (l-i)
        else:
            sScore += (l-i)
    
    if kScore > sScore:
        print("Kevin", kScore)
    elif kScore == sScore:
        print("Draw")
    else:
        print("Stuart",sScore)

if __name__ == '__main__':
