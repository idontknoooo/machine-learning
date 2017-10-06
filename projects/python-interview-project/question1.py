def is_anagram(s, t):

    return sorted(list(s)) == sorted(list(t))



def question1(s, t):

    string_length = len(s)
    pattern_length = len(t)

    for i in range(string_length - pattern_length + 1):
        if is_anagram(s[i: i+pattern_length], t):
            return True
    return False



def main():

    l = ['Jordan', 'Carbon', 'Fantastic', 'Te', 'ABCD', 'udacity']
    t = ['ran', 'bar', 'fan', 'Tree', 'abcd', 'ad']
    ans = [False, True, False, False, False, True]
    
    print 'main: ',
    for i,j in zip(l, t):
        print question1(i, j),

    print '\nans:  ',
    for i in ans:
        print i,



if __name__ == '__main__':

    main()
