''' 
Created Oct 18, 2016

@author: Paul C. Schmitz

Fizz Buzz - A program that prints the numbers from 1 to 100. 
But for multiples of three prints “Fizz” instead of the number 
and for the multiples of five prints “Buzz”. For numbers which 
are multiples of both three and five it prints “FizzBuzz”.
'''

fizz = "Fizz"
buzz = "Buzz"
fizzbuzz = "FizzBuzz"

countby1 = range(0, 101, 1)

def countby15(z):
    for a in range(0, 101, 15):
        try:
            b = z.index(a)
            z.remove(b)
            z.insert(b, fizzbuzz)
        except ValueError:
            pass
    return z

def countby5(y):
    for c in range(0, 101, 5):
        try:
            d = y.index(c)
            y.remove(d)
            y.insert(d, buzz)
        except ValueError:
            pass
    return y 
 
def countby3(x):
    for e in range(0, 101, 3):
        try:
            f = x.index(e)
            x.remove(f)
            x.insert(f, fizz)
        except ValueError:
            pass
    return x

def removezero(zz):
    try:
        zz.remove(fizzbuzz)
    except ValueError:
        pass
    return zz

def printcount(zzz):
    g = iter(countby1)
    for h in g:
        print h    
   
first = countby15(countby1)
second = countby5(first)
third = countby3(second)
fourth = removezero(countby1)
fifth = printcount(countby1)
print fifth
print "Done!"       