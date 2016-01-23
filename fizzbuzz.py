""" Program to find multiples of 2 and 3 """

""" Ask User to enter an integer """

n = input('Enter an integer: ')

""" Define function fizzbuzz """

def fizzbuzz(n):
     for i in range(1,n):
        if i % 2 == 0 and i % 3 == 0:
           print "fizzbuzz"
        elif i % 2 == 0:
           print "fizz"
        elif i % 3 == 0:
           print "buzz"
        else:
           print i
fizzbuzz(n)
