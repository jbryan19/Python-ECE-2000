
#!/usr/bin/python

# ECEGR-2000
# Exercise 2 - buzz.py
# Author: Jack Bryan
def foo(n,z):
    for i in range(1, n+1):
        if i % z == 0:
            print("buzz")
        else:
            print(i)
       
print("Count to 7, buzz on 2's")            
foo(7, 2)
print("Count to 10, buzz on 5's")
foo(10, 5)