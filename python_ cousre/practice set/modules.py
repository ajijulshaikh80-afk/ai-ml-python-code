#Two types of modules in python:
#Build in  modules (means it already written by someone)
#External modules (means created by us or someone else)
import math # this two are built in and third one external
import os
import mymodule
import requests # it also external module tht we get by pip
print(math.sqrt(16)) # math means module and dot means we want to use a fn. from this module and sqrt is name of the fn.
mymodule.hello()
r = requests.get("https://www.google.com")
print(r.text) # this will show code of html google.com


'''https://docs.python.org/3/py-modindex.html this the link to see all types of biult in modules '''

