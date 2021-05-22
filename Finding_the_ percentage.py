if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    
    tmarks = 0.00
    lent = len(student_marks[query_name])
    for i in student_marks[query_name]:
        tmarks = i+tmarks
 
    print('%.2f'%(tmarks/lent))     
