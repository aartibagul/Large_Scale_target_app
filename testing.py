from django.shortcuts import render
from metrix.counters import Counters
import random
import time


#initialize counters
c = Counters("app1", "counter1")
d = Counters("app2", "counters2")


for i in range(10):
    time.sleep(3)
    
    #increment the counters
    c.increment_by(random.randint(1,10))
    d.increment()

