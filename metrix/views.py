from django.shortcuts import render
from django.http import HttpResponse
import datetime
import random
import time
import glob

def index(request):
        
        #Opens all the Counter files
        f_list = glob.glob("/tmp/Counter_*")
        response = ""

        
        if len(f_list) == 0:
            response = "*No counters initialized*"

        else:

            # iterate through all files, get app_name and counter_name from 
            # file_name and get all the counter values from the files
            for f in f_list:
                file_temp = open(f, "r")

                f_name = f.split("_")
                c_list = file_temp.read().split("_")

                for c in c_list:
                    if c != "":
                        c_list1 = c.split("&")
                        response = response + f_name[1]+ "_"+f_name[2] +"="+c_list1[0]
                        response = response + "=" + c_list1[1]
	    	        response += "<br \>"
        
        return HttpResponse(response)
