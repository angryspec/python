'''
Created on Oct 28, 2016

@author: paul
'''
import os
import shelve
import fnmatch

curdir = os.path.dirname(__file__)

class Person(object):
    
    def __init__(self, name):
        self.name = name
    
    # formats text for person name
    def First_Last(self, first, last):
        us = '_'
        seq = (first, last)
        first_last = us.join(seq)
        return first_last
    
    # formats text for data file
    def First_Last_DB(self, first_last):
        dot = '.'
        db = 'db'
        seq = (first_last, db)
        first_last_db = dot.join(seq)
        return first_last_db
    
    # splits first and last names and adds to a list
    def NameSplit(self, first_last):
        splitname = first_last.split('_')
        return splitname
    # creates a person and sends them to Storage
    def Create(self, first, last, born, died, mf, ml, ff, fl):
        first_last = self.First_Last(first, last)
        first_last_db = self.First_Last_DB(first_last)
        self.Storage(first_last, first_last_db, born, died, mf, ml, ff, fl)
    
    # takes info from create and makes data file
    def Storage(self, first_last, first_last_db, born, died, mf, ml, ff, fl):
        first_last = shelve.open(os.path.join(curdir, first_last_db), writeback=True)
        first_last['born'] = born
        first_last['died'] = died
        first_last['mf'] = mf
        first_last['ml'] = ml
        first_last['ff'] = ff
        first_last['fl'] = fl
    
    # views a persons file       
    def View(self, first, last, first_last, first_last_db):
        first_last = shelve.open(os.path.join(curdir, first_last_db))
        print '\n{0} {1}'.format(first, last)
        print '-' * 15
        print 'Born: {0}'.format(first_last.get('born'))
        print 'Died: {0}'.format(first_last.get('died'))
        print 'Mother: {0} {1}'.format(first_last.get('mf'), first_last.get('ml'))
        print 'Father: {0} {1}'.format(first_last.get('ff'), first_last.get('fl'))
        print '-' * 15
    
    # deletes a persons file
    def Delete(self, first, last, first_last_db):
        menu = {}
        menu['1'] = "Yes" 
        menu['2'] = "No"
        while True:
            options = menu.keys()
            options.sort()
            for entry in options:
                print '{0}:'.format(entry), menu[entry]
            selection = raw_input("Please Select: ") 
            if selection =='1': 
                try:
                    os.remove(first_last_db)
                    print "\n{0} {1} Was Deleted\n".format(first, last)
                    break
                except OSError:
                    print '\n{0} {1} Not Found\n'.format(first, last)
                    break 
            elif selection == '2': 
                break
            else:
                print 'Please Enter Yes or No'
    
    # filters files that end in .db 
    def Filter(self):
        cur_dir = os.listdir(curdir)
        lst = []
        for files in cur_dir:
            lst.append(files)
        matches = fnmatch.filter(lst, '*.db')
        return matches
    
    # adds filtered files to a list
    def Matches(self, first_last_db):
        lst = []
        filt = self.Filter()
        for i in filt:
            if i != first_last_db:
                lst.append(i)
        return lst
    
    # gets mother from persons data file
    def getMother(self, first_last, first_last_db):
        first_last = shelve.open(first_last_db)
        mf = first_last.get('mf')
        ml = first_last.get('ml')
        mf_ml = self.First_Last(mf, ml)
        return mf_ml
    
    # gets father from persons data file
    def getFather(self, first_last, first_last_db):
        first_last = shelve.open(first_last_db)
        ff = first_last.get('ff')
        fl = first_last.get('fl')
        ff_fl = self.First_Last(ff, fl)
        return ff_fl
    
    def Tree(self, first, last, first_last, first_last_db):
        first_last = shelve.open(first_last_db)
        m = self.getMother(first_last, first_last_db)
        d = self.getFather(first_last, first_last_db)
        
        mom = self.NameSplit(m)
        dad = self.NameSplit(d)
        #print '{0} {1} is the mother, and {2} {3} is the father of {4} {5}'.format(momfirst, momlast, dadfirst, dadlast, first, last)
            
            
if __name__ == '__main__':
    
    play = Person('play')
    menu = {}
    menu['1'] = "Add Person" 
    menu['2'] = "View Person"
    menu['3'] = "Delete Person"
    menu['4'] = "View Persons Family Tree"
    menu['8'] = "Exit"
    while True:
        options = menu.keys()
        options.sort()
        for entry in options:
            print '{0}:'.format(entry), menu[entry]
        print "-" * 15    
        selection = raw_input("Please Select: ")
        if selection =='1': 
                print ('\nAdd Person\n')
                first = raw_input('Enter First Name: ')
                last = raw_input('Enter Last Name: ')
                born = raw_input('Year Born: ')
                died = raw_input('Year Died: ')
                mf = raw_input('Enter Mother First: ')
                ml = raw_input('Enter Mother Maiden Name: ')
                ff = raw_input('Enter Father First: ')
                fl = raw_input('Enter Father Last: ')
                play.Create(first, last, born, died, mf, ml, ff, fl)
        
        elif selection == '2': 
            print ('\nView Person\n')
            first = raw_input('Enter First Name: ')
            last = raw_input('Enter Last Name: ')
            first_last = play.First_Last(first, last)
            first_last_db = play.First_Last_DB(first_last)
            play.View(first, last, first_last, first_last_db)
        
        elif selection == '3':
            print ('\nDelete Person\n')
            first = raw_input('Enter First Name: ')
            last = raw_input('Enter Last Name: ')
            first_last = play.First_Last(first, last)
            first_last_db = play.First_Last_DB(first_last)
            play.Delete(first, last, first_last_db)
        
        elif selection == '4':
            print ('\nView Persons Family Tree\n')
            first = raw_input('Enter First Name: ')
            last = raw_input('Enter Last Name: ')
            first_last = play.First_Last(first, last)
            first_last_db = play.First_Last_DB(first_last)
            play.Tree(first, last, first_last, first_last_db)
        
        elif selection == '8':
            break    
        
        else:
            print ('\nInvalid Entry!\n')
    
print ('\nExiting...\n')
