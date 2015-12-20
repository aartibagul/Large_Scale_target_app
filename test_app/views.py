from django.shortcuts import render
from test.metrix.counters import Counters
# Create your views here.

c = Counters("app1", "counter1")

d = Counters("app2", "counters2")

for i in range(100):
    c.increment_by(random.randint(1,10))
    d.increment()




