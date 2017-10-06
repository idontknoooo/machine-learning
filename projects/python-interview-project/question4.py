def parent(T, node):

    for row in range(len(T)):
        if T[row][node] == 1:
            return row

    return -1



def question4(T, r, n1, n2):

    tmp1 = parent(T, n1)
    l1 = [tmp1 if tmp1>=0 else '']
    while tmp1 >= 0:
        tmp1 = parent(T, tmp1)
        if tmp1 >= 0:
            l1.append(tmp1) 

    tmp2 = parent(T, n2)
    while tmp2 >= 0:
        if tmp2 in l1:
            return tmp2
        tmp2 = parent(T, tmp2)

    return r



def main():
    
    T =[[0, 1, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [1, 0, 0, 0, 1],
       [0, 0, 0, 0, 0]] 

    print question4(T, 3, 1, 4)
    print question4(T, 3, 1, 3)


    T1 = [[0, 0, 0],
        [1, 0, 1],
        [0, 0, 0]]
    print question4(T1, 1, 0, 2)


    T2 = [[0,0,0,0,0,0,0,0,0],
        [1,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,1,0,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,1,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,0]]
    print question4(T2, 5, 0, 2)
    print question4(T2, 5, 2, 4)
    print question4(T2, 1, 2, 4)
    print question4(T2, 5, 7, 8)
    print question4(T2, 5, 7, 4)
    return 0



if __name__ == '__main__':

    main()
