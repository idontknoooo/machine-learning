# This is a program which find the longest palindrome in a string s


# This helper function
def helper(s, l, r):

    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1; r += 1
    return s[l+1:r]



# Longest palindrome finder
def question2(s):

    res = ""
    for i in xrange(len(s)):
        # odd case, like "aba"
        tmp = helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # even case, like "abba"
        tmp = helper(s, i, i+1)
        if len(tmp) > len(res):
            res = tmp
    return res
  


# Main function with test cases
def main():
    
    # 5 Test Cases
    s = ['ABCCBAD', '', 'a', 'aba', 'ab123321xia']
    for i in s:
        print i, question2(i)
    return 0



# Call main function
if __name__ == '__main__':

    main()
