#!/usr/bin/python3
#this Python File uses the following encoding: utf-8
#Souriya Khaosanga © 2013
#CS300 Fall Term 2013

#sequ Compliance Level 0 ***CHECK***TESTED**
#sequ Compliance Level 1 ***CHECK***TESTED**
#sequ Compliance Level 2 ***Check***TESTED**
 
#Library used for system argument 
from sys import argv;
from sys import exit,argv;

dict = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10 :
			'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:
				'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z'}

#Credit Stack overflow for this Inverse of dictionary
inv_dict = { v:k for k, v in dict.items()}

# from Justin Shuck and http://code.activestate.com/recipes/81611-roman-numerals/
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

def convert_roman(toConvert):
	try:
	   if isinstance(int(toConvert),int):
	        if int(toConvert) <= 0:
	        	return
	        if int(toConvert) > 3000:
	            print 'Integer too big'
	            return
	        return int_to_roman(int(toConvert))
	      
	except ValueError:
	    i = str(toConvert)

	    if roman_to_int(i) == 0:
	        print 'Not a Proper Roman'
	        return    
	    else:
	        return roman_to_int(i)
	


def error():
	print 'status code 1'
	exit(1)

def is_float_int(toCheck):
	if type(toCheck) is float:
		return True
	elif type(toCheck) is int:
		return True
	else:
		return False



#-----------------------------------------------------------------

def convert_alpha(inputVal):
	if type(inputVal) is int:
		modNumber = inputVal % 26
		print dict.get(inputVal)
		return
	elif type_of_value(inputVal) == str and inputVal.__len__() == 1:
		charVal = inv_dict.get(inputVal.upper())
		if charVal == None:
			print 'not valid character'
			return
		print charVal
	
	else:
		print "not  correct alpha input"
		error()

#-----------------------------------------------------------------


def print_file_to_screen(fileToPrint):
	a = open(fileToPrint, "r")
	line = a.readline()
	while line:
		print line
		line = a.readline()
	a.close()

#Convert Backslash to proper form
def back_slash(toChange):
	backN = toChange.replace('\\n','\n')
	backT = backN.replace('\\t', '\t')
	backA = backT.replace('\\a','\a')
	backF = backA.replace('\\f','\f')
	backR = backF.replace('\\r','\r')
	backV = backR.replace('\\v','\v')
	backSlash = backV.replace('\\\\','\\')
	return backSlash

#Credit Stack Overflow with this function
def type_of_value(text):
	try:
		int(text)
		return int
	except ValueError:
		pass

	try:
		float(text)
		return float
	except ValueError:
		pass
	
	return str

#Credit stack Overflow for this function
def convert_num(number):
	try:
		return int(number)
	except ValueError:
		return float(number)

#Find max length of string(s) in an array
def max_length(array):
	maxLength = 0
	for x in range(0,array.__len__()):
		if array[x].__len__() > maxLength:
			maxLength = array[x].__len__()
	return maxLength


def build_seq(beg,end,increment):
	beginning = convert_num(beg)
	ending = convert_num(end)
	increm = convert_num(increment)
	
	while beginning <= ending:
		print beginning
		beginning += increm
	return

def build_alpha_seq(beg,end,increment):
	beginning = convert_num(beg)
	ending = convert_num(end)
	increm = convert_num(increment)
	
	while beginning <= ending:
		print dict.get(beginning)
		beginning += increm
	return



def build_roman_seq(beg,end,increment):
	if is_float_int(beg): 
		return
	if is_float_int(end):
		return
	if is_float_int(increment):
		return


	beginning = convert_roman(beg)
	ending = convert_roman(end)
	increm = convert_roman(increment)
		
	while beginning <= ending:
		print convert_roman(beginning)
		beginning += increm
	return


def build_word_space(word):
	strWord = str(word)
	wordLength = word.__len__()-1
	newString = ""
	for x in range(0,wordLength):
		newString += strWord[x]
		newString += ' '
	newString += strWord[wordLength]
	print newString
	return

def build_equal_width(beg, end, increment):
	

	strBuffer = []
	beginning = convert_num(beg)
	ending = convert_num(end)
	increm = convert_num(increment)
	
	strBeg = str(beginning)
	strEnd = str(ending)	


	while beginning <= ending:
		stringToPrint = str(beginning)
		strBuffer.append(stringToPrint)	
		beginning += increm
	
	maxLength = max_length(strBuffer)

	for x in range(0,strBuffer.__len__()):
		print strBuffer[x].zfill(maxLength)
	return



def build_char_pad(beg, end, increment, char):
	

	strBuffer = []
	beginning = convert_num(beg)
	ending = convert_num(end)
	increm = convert_num(increment)
	
	strBeg = str(beginning)
	strEnd = str(ending)	

	while beginning <= ending:
		stringToPrint = str(beginning)
		strBuffer.append(stringToPrint)	
		beginning += increm
	
	maxLength = max_length(strBuffer)
	
	for x in range(0,strBuffer.__len__()):
		print strBuffer[x].rjust(maxLength,back_slash(char))
	return



#Build implementation for separator
def build_sep_sequence(beg,end,character,increment):


	beginning = convert_num(beg)
	ending = convert_num(end)
	increm = convert_num(increment)
	if beginning > ending:
		return
	elif beginning == ending:
		print beginning
		return
	else:		
		tempString = ''
		while beginning<=ending-increm:
			tempString +=str(beginning)
			tempString +=str(character)
			beginning += increm
		tempString += str(beginning)
		print back_slash(tempString)
		return

def build_format_seq(beg, end, inString, increment):

	beginning = convert_num(beg)
	ending = convert_num(end)
	increm = convert_num(increment)

	while beginning<=ending:
		print (inString  %  beginning)
		beginning+=increm
	return

#Determines if system argument for value to be either a integer or 
#float from beginValue to ending system argument index
def is_argv_number(beginValue):
	lastValue = len(argv)
	for i in range(beginValue,lastValue):
		if type_of_value(argv[i])==str:
			return False
	return True

#***********************************************************************************************
			
# Main part of the program exist below this point	
def main():




	convert_alpha('f')
	convert_alpha('p')
	convert_alpha(25)






#///////////////////////////////////////////////////////////////////////////////////////////////
	#Base case where only program is called
	if len(argv)<=1:
		return	

	#Case where the help is called
	if argv[1] == '--help' or argv[1] == '-h':
		print_file_to_screen("helpfile.txt")
		return

	#Case where the version is called
	if argv[1] == '--version' or argv[1] == '-v':
		print_file_to_screen("versionfile.txt")	
		return

	#Format implementation
	if argv[1]=='-f' or argv[1]=='--format':
		if len(argv) == 4 and is_argv_number(3):
			build_format_seq("1",argv[3],argv[2],"1")

		elif len(argv) == 5 and is_argv_number(3):
			build_format_seq(argv[3],argv[4],argv[2],1)

		elif len(argv)== 6 and is_argv_number(3):
			build_format_seq(argv[3],argv[5],argv[2],argv[4])

		else:
			error()

	#Equal Width implementation
	elif argv[1] == '--equal-width' or argv[1]=='-w':
		if len(argv) == 3 and is_argv_number(2):
			build_equal_width("1",argv[2],"1")

		elif len(argv) ==  4 and is_argv_number(2):
			build_equal_width(argv[2],argv[3],"1")

		elif len(argv) == 5 and is_argv_number(2):
			build_equal_width(argv[2],argv[4],argv[3])

		else:
			error()

	#Separator implementation
	elif argv[1].startswith('--separator'):
		separator = '--separator'
		sepLen = separator.__len__()
		sepString = argv[1]
		sepChar = sepString[sepLen:]
		if len(argv) == 3 and is_argv_number(2):
			build_sep_sequence("1",argv[2],sepChar,"1")

		elif len(argv) == 4 and is_argv_number(2):
			build_sep_sequence(argv[2],argv[3],sepChar,"1")

		elif len(argv) == 5 and is_argv_number(2):
			build_sep_sequence(argv[2],argv[4],sepChar,argv[3])

		else:
			error()
						
	elif argv[1].startswith('-s'):
		separator = '-s'
		sepLen = separator.__len__()
		sepString = argv[1]
		sepChar = sepString[sepLen:]

		if len(argv) == 3 and is_argv_number(2):
			build_sep_sequence("1",argv[2],sepChar,"1")

		elif len(argv) == 4 and is_argv_number(2):
			build_sep_sequence(argv[2],argv[3],sepChar,"1")

		elif len(argv) == 5 and is_argv_number(2):
			build_sep_sequence(argv[2],argv[4],sepChar,argv[3])

		else:
			error()
	
	#Words implementation 
	elif argv[1] == "-W" or argv[1] == '--words':
		
		numOfWords = len(argv)
		for x in range(2, numOfWords):
			build_word_space(argv[x])	


	#Pad with character implementation
	elif argv[1] == "-p" or argv[1] == '--pad':
		if len(argv) == 4 and is_argv_number(3):
			build_char_pad('1',argv[3],'1',argv[2])

		elif len(argv) == 5 and is_argv_number(3):
			build_char_pad(argv[3],argv[4],'1',argv[2])
	
		elif len(argv) == 6 and is_argv_number(3):
			build_char_pad(argv[3],argv[5],argv[4],argv[2])

		else:
			error()

	#Pad with spaces implementation
	elif argv[1] == "-P" or argv[1] == '--pad-spaces':

		if len(argv) == 3 and is_argv_number(3):
			build_char_pad('1',argv[2],'1',' ')
	
		elif len(argv) == 4 and is_argv_number(3):
			build_char_pad(argv[2],argv[3],'1',' ')
		
		elif len(argv) == 5 and is_argv_number(3):
			build_char_pad(argv[2],argv[4],argv[3],' ')

		else:
			error()

	#Basic seq implementation 
	elif len(argv) == 4 and is_argv_number(1):
		build_seq(argv[1],argv[3],argv[2])
	
	elif len(argv) == 3 and is_argv_number(1):
		build_seq(argv[1],argv[2],1)

	elif len(argv) == 2 and is_argv_number(1):
		build_seq(1,argv[1],1)
	
	else:
		error()


if( __name__ == "__main__" ): 
	main()

#*********************************************************************************************
