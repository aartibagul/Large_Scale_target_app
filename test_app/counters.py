

''' 
http://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python



class IterRegistry(type):
    def __iter__(cls):
        return iter(cls._registry)


class Counters:

    __metaclass__ = IterRegistry
    _registry = []

    def __init__(self,*args):
        self._registry.append(self)
        self.counters_dict = {}
        for i in args:
            i = str(i).lower()
            if i not in self.counters_dict:
                self.counters_dict[i]=0
'''

counters_dict = {}
#TODO: 
def add(*args):
    for i in args:
        i = str(i).lower()
        if i not in counters_dict:
            counters_dict[i] = 0


def remove(  *args):
    for i in args:
        i = str(i).lower()
        if i in counters_dict:
            :q   del counters_dict[i]


def increment(  *args):
    for i in args:
        i = str(i).lower()
        if i in counters_dict:
            counters_dict[i] += 1

        else:
            counters_dict[i] = 0


def list_counters( ):
    return counters_dict.keys()


def list_values( ):
    return counters_dict.values()


def list( ):
    return counters_dict.items()


def clear( ):
    return counters_dict.clear()

def len( ):
    return len(counters_dict)

