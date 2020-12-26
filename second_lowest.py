"""
students who got second lowest score
"""

if __name__ == '__main__':
    a= []
    for _ in range(int(input("Total num of students: "))):
        name = input("Name: ")
        score = float(input("Score: "))
        a.append([score, name])

    a.sort()
    b = [i for i in a if i[0] != a[0][0]]
    c = [j for j in b if j[0] == b[0][0]]
    
    c.sort(key=lambda x: x[1])
    for i in range(len(c)):
        print("student who got second lowest score: ", c[i][1])
