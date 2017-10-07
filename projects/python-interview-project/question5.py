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
   
    if not head: return -1
    num = []
    while(head):
        num.append(head.data)
        head = head.next
    return num[-m] if m <= len(num) else -1


# Double_pointer method: use a faster & slower pointer to iterate linked list
def question5(head, m):
    
    if not head: return -1
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



# Main function with test case
def main():
    
    # Test case
    head = Node(4)
    head.next = Node(3)
    head.next.next = Node(5)
    head.next.next.next = Node(10)

    print 'Linked List: ',
    print_ll(head)

    for i in range(6):
        # Call 2 method
        print question5(head, i+1),
        print list_method(head, i+1)


    # Test case 2
    head = Node(4)
    print question5(head, 1),
    print list_method(head, 1)
    

    # Test case 3
    head = None
    print question5(head, 1),
    print list_method(head, 1)


# Call main function
if __name__ == "__main__":

    main()
