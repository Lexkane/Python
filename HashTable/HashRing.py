class ConsistentHashRing(object):

    ''' 
    A wrapper around the SubTree class that lets you manipulate the whole tree at once.
    This class provides access to the root node, and enables you to search the tree
    for the closest match to a value. Iteration and length methods return all stored 
    values in the tree, however.
    Values added to this ConsistentHashRing _must_ be hashable. 
    '''

    def __init__(self, value=None):
        self.head = None if value is None else SubTree(value)

    def add_node(self, value):

        ''' Add a value to the tree as a whole. '''

        if self.head is None:
           self.head = SubTree(value)
        else:
           self.head.add_child(value)

    def remove_node(self, value):

        ''' 
        Remove a value from the tree. 
        Only exact matches may be removed - values not in the tree 
        are ignored. 
        '''

        if self.head is None:
            return 

        self.head = self.head.remove_value(value)
         def find_best_match(self, value):

        '''
        Search for closest match - if exact value exists, it shall return that value, otherwise it will return the closest
        value. If the tree is empty, it returns None.
        Note that 'closest match' here translates to first bigger value than value passed in as parameter here. If an exact
        match is found, it returns that. 
        '''

        key = hash(value)
        current_node = self.head
        best_match, best_match_key = None, float("inf")

        # if tree is empty, return None
        if not self.head:
            return None

        # if tree is not empty, walk through the binary search tree, and update the best_match to reflect the closest but 
        # larger value encountered.

        while current_node is not None:

            # exit if exact match is found, returning that value
            if current_node.key == key:
                return current_node.value

            # if number is bigger, check if it is closer to our target value than the last number, and choose to update
            # accordingly
            if current_node.key > key:

                best_match = current_node.value if abs(current_node.key - key) < abs(best_match_key - key) else best_match
                best_match_key = hash(best_match)

                current_node = current_node.left
                continue

            if current_node.key < key:
                current_node = current_node.right
                continue

        # best_match can still be None if all values in the BST are smaller than the submitted value. In that case,
        # we always return the smallest value in the BST, in line with the principles behind consistent hashing. 

        if best_match:
            return best_match
        else:
            # will always return the smallest value in the BST
            return self.head._find_minimum_subtree_child_value()