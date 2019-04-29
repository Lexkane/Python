class HashTable(object):

    def __init__(self):

        # start with a list of locations
        self._values = [None for item in xrange(256)]
        self._keys = [] # start with no keys, as is right

    def hashfunc(self,key):
        # our hash function.
        return hash(key) % len(self._values)

    def __getitem__(self,key):

        ''' Implements lookup i.e. q[s] calls q.__getitem__(s) '''

        if self._values[self.hashfunc(key)] is not None:
            return self._values[self.hashfunc(key)]
        else:
            return "Not found"

    def __setitem__(self,key,value):

        '''Updates and adds i.e. q[s] = 2 calls q.__setitem__(s,2) '''

        if value is None: 
            raise ValueError('None is not permitted as a value.')

        # if there's never been a value, then add key and set value
        if self._values[self.hashfunc(key)] is None:
            self._keys.append(key)
            self._values[self.hashfunc(key)] = value

        # if there **is** a value already, then update the old one
        else:
            if key in self._keys:
                self._values[self.hashfunc(key)] = value