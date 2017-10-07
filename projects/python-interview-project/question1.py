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



# Main function
def main():

    # Test Cases
    l = ['Jordan', 'Carbon', 'Fantastic', 'Te', 'ABCD', 'udacity']
    t = ['ran', 'bar', 'fan', 'Tree', 'abcd', 'ad']
    # Answers to test cases
    ans = [False, True, False, False, False, True]
    
    # Print my solution
    print 'main: ',
    for i,j in zip(l, t):
        print question1(i, j),

    # Print standard answer
    print '\nans:  ',
    for i in ans:
        print i,



# Call Main function
if __name__ == '__main__':

    main()
