class SubTree(object):

    '''
    A class that implements a subtree in our binary search tree. This subtree can be either a node, a node with leaf nodes, or a node with other other subtrees as children. 

    Methods for removal and insertion are defined here. Lookup is not provided as we only care about that when we have access to a dedicated root node. 
    '''

    def __init__(self, value, left=None, right=None):

        '''
        @param: value [Any]: The raw value you wish to insert. Must implement comparison.
        @param: left, right [Node]: Left and right children of this node.
        '''

        self.value, self.key = value, hash(value)
        self.left, self.right = left, right

	def add_child(self, value):

        ''' 
        Recursively add a child node with the defined value.
        Duplicate values are excluded in this tree.
        '''

        key = hash(value)

        if key == self.key:
           return 

        if key > self.key:

            if self.right is None:
                self.right = SubTree(value)
            else:
                self.right.add_child(value)

        if key < self.key:

            if self.left is None:
                self.left = SubTree(value)
            else:
                self.left.add_child(value)      
	def remove_value(self, value):
        '''
        Removes a value from this node and its subtree. 
        Returns the new node that should take the place of the node 
        that was removed.
        '''

        key = hash(value)

        if key == self.key:

            # if leaf node, remove oneself
            if self.left is None and self.right is None:
                return None

            # the following two cases return whichever child node is 
            # extant for a one-child parent.

            if self.left is None and self.right is not None:
                return self.right

            if self.right is None and self.left is not None:
                return self.left

            # case where neither left or right child is empty
            if self.right is not None and self.left is not None:
                # copy the value of the first in-order successor, 
                # then delete the first in-order successor node.
                self.value = self._find_in_order_successor()
                self.right = self.right.remove_value(self.value)
                return self
        else:
             if self.left is not None:
                 self.left = self.left.remove_value(value)
             if self.right is not None:
                 self.right = self.right.remove_value(value)
             return self #