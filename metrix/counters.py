''' 
http://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python
'''
'''
class Iter_Registry(type):
    def __iter__(cls):
        return iter(_registry)

    def __len__(cls):
        return len(_registry)

    #def __getitem__(cls,val):
    #    return cls._registry[val]

'''

import datetime

class Counters:
    
    #__metaclass__ = Iter_Registry
    #_registry = []

    def __init__(self, app_name, counter_name):
        #_registry.append(self)
        #print(len(_registry))
        self.file_name = "/tmp/Counter_"+ app_name + "_" + counter_name 
        f = open(self.file_name, "w+")
        to_write= "_0&"+ str(datetime.datetime.now())
        f.write(to_write)
        f.close()
        self.app = app_name
        self.name = counter_name
        self.value = 0



    def increment(self):
        self.value += 1
        
        
        f = open(self.file_name, "a")
        to_write = "_" + str(self.value)+ "&"+ str(datetime.datetime.now())

        
        f.write(to_write)
        f.close()

    def increment_by(self, value):
       
        self.value += value
        f = open(self.file_name, "a")
        to_write = "_" + str(self.value)+"&"+ str(datetime.datetime.now()) 
        f.write(to_write)
        f.close()

    def get_value(self):
        return self.value

    def get_name(self):
        return self.name

    def get_app(self):
        return self.app



