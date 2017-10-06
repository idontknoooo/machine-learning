class Node(object):

    def __init__(self, data):

        self.data = data
        self.next = None
        


def print_ll(head):

    while(head):
        print head.data,
        head = head.next
    print ''




def list_method(head, m):
    
    num = []
    while(head):
        num.append(head.data)
        head = head.next
    return num[-m] if m <= len(num) else -1


# double_pointer
def question5(head, m):

    first = head
    second = head
    while m>0 and first:
        first = first.next
        m -= 1
    if m>0: return -1
    while first:
        second = second.next
        first = first.next
    
    return second.data



def main():
    
    head = Node(4)
    head.next = Node(3)
    head.next.next = Node(5)
    head.next.next.next = Node(10)

    print 'Linked List: ',
    print_ll(head)

    for i in range(6):
        print question5(head, i+1),
        print list_method(head, i+1)



if __name__ == "__main__":

    main()
