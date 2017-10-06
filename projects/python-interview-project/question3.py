import sys
def question3(G):
    
    size = len(G)
    if size==1: 
        single = {}
        for i in G:
            single[i] = []
            print single
            return single

    vertex = [key for key in G]
    matrix = [[sys.maxint for i in range(size)] for j in range(size)]

    visited_row = [0]

    #print vertex

    for node, row in zip(G, range(size)):   
        for i in G[node]:
            column = vertex.index(i[0]) 
            matrix[row][column] = i[1]

    #print matrix
    mst = {}
    for times in range(size):
        tmp_min = sys.maxint 
        tmp_row = -1
        tmp_col = -1
        for i in visited_row:
            for j in range(size):
                if j not in visited_row and tmp_min > matrix[i][j]:
                    tmp_min = matrix[i][j]
                    tmp_row = i
                    tmp_col = j

        visited_row.append(tmp_col)
        if vertex[tmp_row] not in mst and vertex[tmp_row] != vertex[tmp_col]:
            mst[vertex[tmp_row]] = []
            mst[vertex[tmp_row]].append((tmp_min, vertex[tmp_col]))
        elif vertex[tmp_row] != vertex[tmp_col]:
            mst[vertex[tmp_row]].append((tmp_min, vertex[tmp_col]))

    print mst
    return mst



def main():

    G = {'A': [('B', 2), ('D', 4)],
    'B': [('A', 2), ('C', 5), ('D', 3)],
    'C': [('B', 5), ('D', 2)],
    'D': [('A', 4), ('B', 3), ('C', 2)]}
    question3(G)


    G1 = {'A': [('B', 2)],
     'B': [('A', 2), ('C', 5)], 
      'C': [('B', 5)]}
    question3(G1)


    G2 = {'A': [('B', 2), ('C', 3), ('D', 3)],
    'B': [('A', 2), ('C', 4), ('E', 3)],
    'C': [('A', 3), ('B', 4), ('E', 1), ('F', 6)],
    'D': [('A', 3), ('F', 7)],
    'E': [('B', 3), ('C', 1), ('F', 8)],
    'F': [('C', 6), ('D', 7), ('E', 8), ('G', 9)],
    'G': [('F', 9)]}
    question3(G2)


    G3 = {}
    question3(G3)
    

    G4 = {'A': []}
    question3(G4)


    G5 = {'S': [('OS', 4)],
    'OS': [('S', 4)]}
    question3(G5)
    return 0

if __name__ == "__main__":

    main()
