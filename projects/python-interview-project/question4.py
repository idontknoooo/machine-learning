# This is a program find least common ancester given two node

# A helper function calculate the parent of a given node
def parent(T, node):

    for row in range(len(T)):
        if T[row][node] == 1:
            return row

    # if not find return -1 (when node == root)
    return -1


# Question4
def question4(T, r, n1, n2):

    # Calculate all parents for n1 and store them in a list
    tmp1 = parent(T, n1)
    l1 = [tmp1 if tmp1>=0 else '']
    while tmp1 >= 0:
        tmp1 = parent(T, tmp1)
        if tmp1 >= 0:
            l1.append(tmp1) 

    # Find the parent of n2 which appear first in n1's parent list
    tmp2 = parent(T, n2)
    while tmp2 >= 0:
        if tmp2 in l1:
            # return first appear common parent
            return tmp2
        tmp2 = parent(T, tmp2)

    # Otherwise return root
    return r



# Main function with test case
def main():
    
    # Test Case

    # Udacity case
    T =[[0, 1, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [1, 0, 0, 0, 1],
       [0, 0, 0, 0, 0]] 

    print question4(T, 3, 1, 4)
    print question4(T, 3, 1, 3)


    # Simple case
    T1 = [[0, 0, 0],
        [1, 0, 1],
        [0, 0, 0]]
    print question4(T1, 1, 0, 2)


    # A quite complicated case
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




# Call main function
if __name__ == '__main__':

    main()
