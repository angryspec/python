a = 'Enter a word to see if its a palindrome: '
b = 'Check another? y/n: '
y = 'y' or 'yes' or 'Yes'
n = 'n' or 'no' or 'No'

def isornot(raw_a):
    if raw_a == raw_a[::-1]:
        print raw_a, 'is a palindrome'
    else:
        print raw_a, 'is not a palindrome'
    checkagain(raw_input(b))

def checkagain(raw_b):
    if raw_b == y:
        isornot(raw_input(a))
    elif raw_b == n:
        print "Done!"
    else:
        print 'Please enter either y or n' 
        checkagain(raw_input(b))
    return "Done!"
    
isornot(raw_input(a))