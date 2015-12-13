
''' 
http://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python
'''



class Dictionary(type):
    def __iter__(cls):
        return iter(cls._registry)

    def __len__(cls):
        return len(cls._registry)

class Counters:
    
    __metaclass__ = Dictionary
    _registry = []

    def __init__(self, name):
        self._registry.append(self)
        self.name = name
        self.value = 0

    def increment(self):
        self.value += 1

    def increment_by(self, value):
        self.value += value

    def get_value(self):
        return self.value

    def get_name(self):
        return self.name




