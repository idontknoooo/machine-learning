###################################################################################
##############################---Question1---######################################
###################################################################################



# This is a program check whether the anagram of string t is a substring of string s

# Check whether two string are anagram to each other
def is_anagram(s, t):

    return sorted(list(s)) == sorted(list(t))



# Main function for question 1
def question1(s, t):

    string_length = len(s)
    pattern_length = len(t)

    # Go through the substring of s to check if any of the substring (same size with t) is an anagram to t
    for i in range(string_length - pattern_length + 1):
        if is_anagram(s[i: i+pattern_length], t):
            return True
    return False



###################################################################################
##############################---Question2---######################################
###################################################################################



# This is a program which find the longest palindrome in a string s


# This helper function
def helper(s, l, r):
    
    # Check the longest palindrome for given an element in the string
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1; r += 1
    return s[l+1:r]



# Longest palindrome finder
def question2(s):

    res = ""
    for i in range(len(s)):
        # odd case, like "aba"
        tmp = helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # even case, like "abba"
        tmp = helper(s, i, i+1)
        if len(tmp) > len(res):
            res = tmp
    return res



###################################################################################
##############################---Question3---######################################
###################################################################################



# This is a program find minimum spanning tree(mst) from a graph

# Import sys for sys.maxint
import sys


# Question3
def question3(G):
    
    # Return the edge size of G
    size = len(G)
    
    # Handle the one node case
    if size==1: 
        single = {}
        for i in G:
            single[i] = []
            print single
            return single

    # A vertex list for all vertex
    vertex = [key for key in G]
    # Convert input dict to matrix for further calculation
    matrix = [[sys.maxint for i in range(size)] for j in range(size)]

    visited_row = [0]

    # Initialize the matrix
    for node, row in zip(G, range(size)):   
        for i in G[node]:
            column = vertex.index(i[0]) 
            matrix[row][column] = i[1]

    # Initialize MST
    mst = {}
    for times in range(size):
        tmp_min = sys.maxint 
        tmp_row = -1
        tmp_col = -1
        # Create MST using Prim's algorithm
        for i in visited_row:
            for j in range(size):
                if j not in visited_row and tmp_min > matrix[i][j]:
                    tmp_min = matrix[i][j]
                    tmp_row = i
                    tmp_col = j

        visited_row.append(tmp_col) # add into visited list
        # Append into MST
        if vertex[tmp_row] not in mst and vertex[tmp_row] != vertex[tmp_col]:
            mst[vertex[tmp_row]] = []
            mst[vertex[tmp_row]].append((tmp_min, vertex[tmp_col]))
        elif vertex[tmp_row] != vertex[tmp_col]:
            mst[vertex[tmp_row]].append((tmp_min, vertex[tmp_col]))

    print mst
    return mst



###################################################################################
##############################---Question4---######################################
###################################################################################



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
    
    
    
###################################################################################
##############################---Question5---######################################
###################################################################################



# This is a program find the m'th element from tail of a linked list

# Node class for linked list
class Node(object):

    def __init__(self, data):

        self.data = data
        self.next = None
        

# A function help visualization, print linked list
def print_ll(head):

    while(head):
        print head.data,
        head = head.next
    print ''




# Method 1: Store in list and access using []
def list_method(head, m):
   
    if not head: return None
    num = []
    while(head):
        num.append(head.data)
        head = head.next
    return num[-m] if m <= len(num) else None


# Double_pointer method: use a faster & slower pointer to iterate linked list
def question5(head, m):
    
    if not head: return None
    first = head
    second = head
    while m>0 and first:
        first = first.next
        m -= 1
    if m>0: return None
    while first:
        second = second.next
        first = first.next
    
    return second.data
    
    
    
    
    
    
###################################################################################
###################################################################################
###################################################################################   
###################################################################################
###################################################################################
###################################################################################







# Main function
def main():



    ###################################################################################
    ###################################################################################
    ###################################################################################
    
    
    
    print "Question1"
    print '###################################################################################'
    # Test Cases
    l = ['Jordan', 'Carbon', 'Fantastic', 'Te', 'ABCD', 'udacity']
    t = ['ran', 'bar', 'fan', 'Tree', 'abcd', 'ad']
    # Answers to test cases
    # Answer: [False, True, False, False, False, True]
    ans = [False, True, False, False, False, True]
    
    # Print my solution
    print 'main: ',
    for i,j in zip(l, t):
        print question1(i, j),

    # Print standard answer
    print '\nans:  ',
    for i in ans:
        print i,
    print "\n\n"    
        
        
        
    ###################################################################################
    ###################################################################################
    ###################################################################################



    print "Question2"
    print '###################################################################################'
    # 5 Test Cases
    s = ['ABCCBAD', '', 'a', 'aba', 'ab123321xia']
    for i in s:
        # Answer: 'ABCCBA', '', 'a', 'aba', '123321'
        print 'string: ', i, '\n   LPD: ', question2(i)
    print "\n" 



    ###################################################################################
    ###################################################################################
    ###################################################################################
    
    
    
    print "Question3"
    print '###################################################################################'
    # Test Cases

    # Udacity case
    G = {'A': [('B', 2), ('D', 4)],
    'B': [('A', 2), ('C', 5), ('D', 3)],
    'C': [('B', 5), ('D', 2)],
    'D': [('A', 4), ('B', 3), ('C', 2)]}
    print 'Origin: ', G
    print '   MST: ',
    # Answer:  {'A': [(2, 'B')], 'B': [(3, 'D')], 'D': [(2, 'C')]}
    question3(G)
    print ""


    # A simple case
    G1 = {'A': [('B', 2)],
     'B': [('A', 2), ('C', 5)], 
      'C': [('B', 5)]}
    print 'Origin: ', G1
    print '   MST: ',
    # Answer:  {'A': [(2, 'B')], 'B': [(5, 'C')]}
    question3(G1)
    print ""

    # A complicated case
    G2 = {'A': [('B', 2), ('C', 3), ('D', 3)],
    'B': [('A', 2), ('C', 4), ('E', 3)],
    'C': [('A', 3), ('B', 4), ('E', 1), ('F', 6)],
    'D': [('A', 3), ('F', 7)],
    'E': [('B', 3), ('C', 1), ('F', 8)],
    'F': [('C', 6), ('D', 7), ('E', 8), ('G', 9)],
    'G': [('F', 9)]}
    print 'Origin: ', G2
    print '   MST: ',
    # Answer:  {'A': [(2, 'B'), (3, 'C'), (3, 'D')], 'C': [(1, 'E'), (6, 'F')], 'F': [(9, 'G')]}
    question3(G2)
    print ""

    # Empty case
    G3 = {}
    print 'Origin: ', G3
    print '   MST: ',
    # Answer:  {}
    question3(G3)
    print ""

    # One node case
    G4 = {'A': []}
    print 'Origin: ', G4
    print '   MST: ',
    # Answer:  {'A': []}
    question3(G4)
    print ""

    # Two node case
    G5 = {'S': [('OS', 4)],
    'OS': [('S', 4)]}
    print 'Origin: ', G5
    print '   MST: ',
    # Answer:  {'S': [(4, 'OS')]}
    question3(G5)
    print "\n"
    
    
    
    ###################################################################################
    ###################################################################################
    ###################################################################################
    
    
    print "Question4"
    print '###################################################################################'
    # Test Case

    # Udacity case
    T =[[0, 1, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [1, 0, 0, 0, 1],
       [0, 0, 0, 0, 0]] 

    # Answer: 3
    print question4(T, 3, 1, 4), 'ans: 3'
    # Answer: 3
    print question4(T, 3, 1, 3), 'ans: 3'


    # Simple case
    T1 = [[0, 0, 0],
        [1, 0, 1],
        [0, 0, 0]]
    # Answer: 1
    print question4(T1, 1, 0, 2), 'ans: 1'


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
    # Answer: 1
    print question4(T2, 5, 0, 2), 'ans: 1'
    # Answer: 3
    print question4(T2, 5, 2, 4), 'ans: 3'
    # Answer: 3
    print question4(T2, 1, 2, 4), 'ans: 3'
    # Answer: 6
    print question4(T2, 5, 7, 8), 'ans: 6'
    # Answer: 5
    print question4(T2, 5, 7, 4), 'ans: 5'
    # Answer: 5
    print question4(T2, 5, 5, 5), 'ans: 5'
    
    print "\n"
    
    ###################################################################################
    ###################################################################################
    ###################################################################################
    
    
    print "Question5"
    print '###################################################################################'
    # Test case
    head = Node(4)
    head.next = Node(3)
    head.next.next = Node(5)
    head.next.next.next = Node(10)

    print 'Linked List: ',
    print_ll(head)

    # Answer: 10, 5, 3, 4, None, None
    for i in range(6):
        # Call 2 method
        print 'Double pointer: ', question5(head, i+1), '\n          list: ',
        print list_method(head, i+1)
    print ""

    # Test case 2
    head = Node(4)
    print 'Linked List: ',
    print_ll(head)
    
    # Answer: 4
    print 'Double pointer: ', question5(head, 1), '\n          list: ',
    print list_method(head, 1)
    print ""    

    # Test case 3
    head = None
    print 'Linked List: ',
    print_ll(head)
    
    # Answer: None
    print 'Double pointer: ', question5(head, 1), '\n          list: ',
    print list_method(head, 1)
    

# Call Main function
if __name__ == '__main__':

    main()
