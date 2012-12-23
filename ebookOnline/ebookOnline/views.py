'''
Created on Dec 23, 2012

@author: kevin
'''
from django.http import HttpResponse

def hello(request):
    return HttpResponse("hello from kevin")