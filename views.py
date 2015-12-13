from django.shortcuts import render
from django.http import HttpResponse
from counters import Counters


c = Counters("a")
c.increment_by(15)

d = Counters("d")
d.increment()

def index(request):

        response = ""
        if len(Counters) == 0:
            request = "*No counters initialized*"

        else:
            for c in Counters:
                response = response + c.get_name() +"="+str(c.get_value())
                response += "<br \>"
        
        return HttpResponse(response)
