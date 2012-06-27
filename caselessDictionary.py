class CaselessDictionary(dict):
    """A dictionary with case-insensitive keys.
    
    A dictionary that is case-insensitive when searching, but also preserves 
    the keys as inserted.
    """
    
    def __init__(self, initval={}):
        if isinstance(initval, dict):
            for key, value in initval.iteritems():
                self.__setitem__(key, value)
        elif isinstance(initval, list):
            for (key, value) in initval:
                self.__setitem__(key, value)
            
    def __contains__(self, key):
        return dict.__contains__(self, key.lower())
  
    def __getitem__(self, key):
        return dict.__getitem__(self, key.lower())['val'] 
  
    def __setitem__(self, key, value):
        return dict.__setitem__(self, key.lower(), {'key': key, 'val': value})

    def get(self, key, default=None):
        try:
            v = dict.__getitem__(self, key.lower())
        except KeyError:
            return default
        else:
            return v['val']
    
    def items(self):
        return [(v['key'], v['val']) for v in dict.itervalues(self)]
    
    def keys(self):
        return [v['key'] for v in dict.itervalues(self)]
    
    def values(self):
        return [v['val'] for v in dict.itervalues(self)]
    
    def iteritems(self):
        for v in dict.itervalues(self):
            yield v['key'], v['val']
        
    def iterkeys(self):
        for v in dict.itervalues(self):
            yield v['key']
        
    def itervalues(self):
        for v in dict.itervalues(self):
            yield v['val']