# Converts int to roman numerials and vice verca.
# Justin Shuck 2013
# This program was build from the website 
# http://code.activestate.com/recipes/81611-roman-numerals/
# Justin Shuck made modifications to that code from the website.

from sys import exit,argv

numeral_map = zip(
    (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
    ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
)

def int_to_roman(i):
    result = []
    for integer, numeral in numeral_map:
        count = int(i / integer)
        result.append(numeral * count)
        i -= integer * count
    return ''.join(result)

def roman_to_int(n):
    n = unicode(n).upper()

    i = result = 0
    for integer, numeral in numeral_map:
        while n[i:i + len(numeral)] == numeral:
            result += integer
            i += len(numeral)
    return result

if __name__ == '__main__':
	
	try:
	   if isinstance(int(argv[1]),int):
	        if int(argv[1]) <= 0:
	             exit(1)
	        if int(argv[1]) > 3000:
	             print 'Integer too big'
	             exit(1)
	        print int_to_roman(int(argv[1]))
	        exit(1)
	except ValueError:
	    i = str(argv[1])

	    if roman_to_int(i) == 0:
	        print 'error'
	        exit(1)    
	    else:
	        print roman_to_int(i)	  
