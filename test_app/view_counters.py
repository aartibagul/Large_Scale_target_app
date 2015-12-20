from django.http import HttpResponse
import counters

counters.add("test1", "test2", "test3", "test4")

for i in range(30):
    counters.increment("test1")
def display_counters(request):
    if len(counters.counters_dict) == 0:
        return HttpResponse("<h1>*No counters added*</h1>")
    else:
        response = '<table border="1" style="width:20%">'
        for c in counters.counters_dict:
            response = response + "<tr>" + "<td>" + c + "</td>" +  "<td>" + str(counters.counters_dict[c]) + "</td>" + "</tr>" 
        
        response += "</table>"
        return HttpResponse(response)
