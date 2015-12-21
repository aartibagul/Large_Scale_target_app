import datetime

class Counters:
    

    def __init__(self, app_name, counter_name):
        

        #creates a file Counter_appname_countername and stores a value of 0
        self.file_name = "/tmp/Counter_"+ app_name + "_" + counter_name 
        f = open(self.file_name, "w+")
        to_write= "_0&"+ str(datetime.datetime.now())
        f.write(to_write)
        f.close()
        self.app = app_name
        self.name = counter_name
        self.value = 0



    def increment(self):
        # increments counter value by one and saves it to a file
        self.value += 1

        f = open(self.file_name, "a")
        to_write = "_" + str(self.value)+ "&"+ str(datetime.datetime.now())
    
        f.write(to_write)
        f.close()

    def increment_by(self, value):
        # increments counter by value and saves it to a file

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



