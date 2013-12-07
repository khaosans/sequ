#!/usr/bin/python3
#this Python File uses the following encoding: utf-8
#Souriya Khaosanga © 2013
#CS300 Fall Term 2013

#sequ Compliance Level 0 ***CHECK***TESTED**
#sequ Compliance Level 1 ***CHECK***TESTED**
#sequ Compliance Level 2 ***CHECK***TESTED**
 
#Library used for system argument 
from sys import argv;
from sys import exit,argv;
import re;
import string;


dict = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10 :
			'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:
				'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z'}

#Credit Stack overflow for this Inverse of dictionary
inv_dict = { v:k for k, v in dict.items()}


#Credit Sean Debellis
def is_roman(string):
	romanUpREStr = r'M*(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

	if re.match(romanUpREStr, string, re.IGNORECASE):
		return True
	else:
		return False

#Credit Sean Debellis
def determine_numeral_type(string):

    romanUpREStr = r'M*(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    romanLoREStr = r'm*(cm|cd|d?c{0,3})(xc|xl|l?x{0,3})(ix|iv|v?i{0,3})$'
    alphaUpREStr = r'[A-Z]{1}$'
    alphaLoREStr = r'[a-z]{1}$'
    integerREStr = r'-?[0-9]+$'
    floatREStr = r'[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'

    numeralType = None

    if re.match(integerREStr, string):
        numeralType = 'INTEGER'
    elif re.match(floatREStr, string):
        numeralType = 'FLOAT'
    elif re.match(alphaUpREStr, string):
        numeralType = 'ALPHA'
    elif re.match(alphaLoREStr, string):
        numeralType = 'alpha'
    elif re.match(romanUpREStr, string):
        numeralType = 'ROMAN'
    elif re.match(romanLoREStr, string):
        numeralType = 'roman'
    
    return numeralType


# from Justin Shuck and http://code.activestate.com/recipes/81611-roman-numerals/
#-----------------------------------------------------------------
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

def convert_romanint_to_int(stringValue):
	if is_roman(stringValue) == True:
		number = convert_roman(stringValue)
		return number
	elif type_of_value(stringValue) == int:
		number = convert_num(stringValue)
		return number
	else:
		error()
	
#-----------------------------------------------------------------

def build_inferred_seq(beg,end,increm):

	if is_int_or_float(beg) == True and is_int_or_float(end) == True and is_int_or_float(increm) == True:
		build_seq(beg, end, increm)

	elif is_roman(end) == True:
		build_roman_seq(beg,end,increm,end.isupper())
	
	elif type_of_value(end) == int:
		build_seq_from_roman(beg,end,increm)

	
	else:
		error()

#checks the input to see if it's roman or integer
def try_roman(inputString):
	if type_of_value(str(inputString)) == float:
		return None
	try:
		return int(inputString)
	except ValueError:
		if is_roman(inputString) == True:
			return str(inputString)
	

#takes input of Roman numerals and integers
def build_roman_seq(beg,end, increment, uppercase):

	beg = try_roman(beg)
	end = try_roman(end)
	increment = try_roman(increment)

	if beg == None or end == None or increment == None:
		error()

	if is_roman(str(beg)) == True:
		beg = convert_roman(beg)

	if is_roman(str(end)) == True:
		end = convert_roman(end)

	if is_roman(str(increment)) == True:
		increment = convert_roman(increment)

	while beg <= end:
		if uppercase == False:
			print convert_roman(beg).lower()
		if uppercase == True:
			print convert_roman(beg)
		beg += increment
	return

#takes input of roman numerals or integer and outputs an integer
def build_seq_from_roman(beg, end, increment):

	beg = try_roman(beg)
	end = try_roman(end)
	increment = try_roman(increment)

	if beg == None or end == None or increment == None:
		error()

	if is_roman(str(beg)) == True:
		beg = convert_roman(beg)

	if is_roman(str(end)) == True:
		end = convert_roman(end)

	if is_roman(str(increment)) == True:
		increment = convert_roman(increment)

	while beg <= end:
		print beg
		beg += increment
	return


def error():
	print 'status code 1'
	exit(1)



def convert_alpha(inputVal):
	if type(inputVal) is int:
		modNumber = inputVal % 26
		return dict.get(inputVal)
		return
	elif type_of_value(inputVal) == str and inputVal.__len__() == 1:
		charVal = inv_dict.get(inputVal.upper())
		if charVal == None:
			print 'not valid character'
			return
		return charVal
	
	else:
		print "not  correct alpha input"
		error()

def build_alpha_seq(beg, end, increment, uppercase):
	

	beg = convert_alpha(beg)
	end = convert_alpha(end)

	increment = convert_alpha(increment)

	while beg <= end:
		if uppercase == True:
			print convert_alpha(beg)
		if uppercase == False:
			print convert_alpha(beg).lower()	
		beg += increment
	return



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

#Check the argv input such that it is equal to the type
def is_argv_equalto(equalToType):
	lastValue = len(argv)
	for i in range(3, lastValue):
		if determine_numeral_type(argv[i]) != equalToType:
			return False
	return True

def is_argv_number(beginValue):
	lastValue = len(argv)
	for i in range(beginValue,lastValue):
		if type_of_value(argv[i])==str:
			return False
	return True
#Determines if the system arguments are integer or roman numeral
def is_argv_int_or_roman(beginValue):
	lastValue = len(argv)
	for i in range(beginValue,lastValue):
		if type_of_value(argv[i])==str  and is_roman(argv[i]) == False:
			return False
	return True

#Determine if the value is a float or and integer
def is_int_or_float(value):
	if type_of_value(value) == int or type_of_value(value) == float:
		return True
	else: 
		return False

#determine if the value is a integer or a roman value		
def is_int_or_roman(value):
	if is_roman(value) == True:
		return True
	elif type_of_value(value) == int:
		return True
	else:
		return False





#Function takes only integers or floating points as arguments		
def print_number_line(beg, increm, filename, case, sep):

	lineNumber = beg
	try:
		with open(filename) as inFile:
			
			for line in inFile:
				if case == 'roman':
					print str(convert_roman(lineNumber)).lower() + back_slash(sep) + line.rstrip()
					lineNumber += increm  
				elif case == 'ROMAN':
					print str(convert_roman(lineNumber)) + back_slash(sep) + line.rstrip()
					lineNumber += increm         
				elif case == 'ALPHA':
					lineNumber = (lineNumber % 27) 
					if lineNumber == 0:
						lineNumber += 1
					print str(convert_alpha(lineNumber)) + back_slash(sep) + line.rstrip()
					lineNumber += increm 
				elif case == 'alpha':
					lineNumber = (lineNumber % 27) 
					if lineNumber == 0:
						lineNumber += 1
					print str(convert_alpha(lineNumber )).lower() + back_slash(sep) + line.rstrip()
					lineNumber += increm
				elif case == 'FLOAT':
					print str(float(lineNumber)) + back_slash(sep) + line.rstrip()
					lineNumber += increm 
				elif case == 'INTEGER':
					print str(lineNumber) + back_slash(sep) + line.rstrip()
					lineNumber += increm
				else:
					error()
		exit(1)	
	except IOError as e:
		print 'No such file exists'.format(e.errno, e.strerror)
	except ValueError:
		print 'value error'
	except:
		raise

		

def inferred_print_line(beg, increm, filename, sep):

	if is_roman(beg) == True and is_roman(increm) == True:
		if beg.isupper() == True and increm.isupper() == True:
			print_number_line(convert_romanint_to_int(beg),convert_romanint_to_int(increm),filename, 'ROMAN', sep)

	
		elif beg.islower() == True and increm.islower() == True:
			print_number_line(convert_romanint_to_int(beg), convert_romanint_to_int(increm), filename, 'roman', sep)

		else:
			error()

	elif determine_numeral_type(beg) == 'alpha' and determine_numeral_type(increm) == 'alpha':
		print_number_line(convert_alpha(beg), convert_alpha(increm), filename, 'alpha', sep)

	elif determine_numeral_type(beg) == 'ALPHA' and determine_numeral_type(increm) == 'ALPHA':
		print_number_line(convert_alpha(beg), convert_alpha(increm), filename, 'ALPHA', sep)

	elif determine_numeral_type(beg) == 'FLOAT' and determine_numeral_type(increm) == 'FLOAT':
		print_number_line(float(beg), float(increm), filename, 'FLOAT', sep)

	elif determine_numeral_type(beg) == 'INTEGER' and determine_numeral_type(increm) == 'INTEGER':
		print_number_line(int(beg), int(increm), filename, 'INTEGER', sep)

	else:
		error()				

def number_lines(beg, increm, fileName, case, sep):
	if case == 'roman':
		if is_int_or_roman(beg) == True and is_int_or_roman(increm) == True:
			print_number_line(convert_romanint_to_int(beg),convert_romanint_to_int(increm),fileName, 'roman', sep)

	elif case == 'ROMAN':
		if is_int_or_roman(beg) == True and is_int_or_roman(increm) == True:
			print_number_line(convert_romanint_to_int(beg),convert_romanint_to_int(increm),fileName, 'ROMAN', sep)


	elif case == 'ALPHA':
		if determine_numeral_type(beg) == 'ALPHA' and determine_numeral_type(increm) == 'ALPHA':
			print_number_line(convert_alpha(beg),convert_alpha(increm),fileName, 'ALPHA', sep)

	elif case == 'alpha':
		if determine_numeral_type(beg) == 'alpha' and determine_numeral_type(increm) == 'alpha':
			print_number_line(convert_alpha(beg),convert_alpha(increm),fileName, 'alpha', sep)

	elif case == 'FLOAT':
		if determine_numeral_type(beg) == 'FLOAT' and determine_numeral_type(increm) == 'FLOAT':
			print_number_line(float(beg), float(increm), fileName, 'FLOAT', sep)
	elif case == 'INTEGER':
		if determine_numeral_type(beg) == 'INTEGER' and determine_numeral_type(increm) == 'INTEGER':
			print_number_line(int(beg), int(increm), fileName, 'INTEGER', sep)
	else:
		error()

def increment_by_one(matchingValue):
	if is_roman(matchingValue) == True and matchingValue.isupper() == True:
			return 'I'
	elif is_roman(matchingValue) == True and matchingValue.islower() == True:
			return 'i'
	elif type_of_value(matchingValue) == float:
		return '1.0'
	elif type_of_value(matchingValue) == int:
		return '1'
	else:
		error()

#Between these brackets is used for unit testing of functions
#***********************************************************************************************
#def number_lines(beg, increm, fileName, printType, sep):			
# Main part of the program exist below this point	
def main():



	'''
	print_number_line(1,2,"test.txt", 'roman', '\t')
	
	print_number_line(1,2,"test.txt", 'ROMAN', '\t')
	print_number_line(1,1,"test.txt", 'ALPHA', '\t')

	print_number_line(1,2,"test.txt", 'alpha', '\t')
	print_number_line(1,2,"test.txt", 'FLOAT', '\t')
	print_number_line(1,2,'test.txt', 'INTEGER', '\t')
	'''
	#inferred_print_line('I','II', 'test.txt', '\t')
	#inferred_print_line('i','ii','test.txt', '\t')
	#inferred_print_line('a','a','test.txt', '\t')
	#inferred_print_line('A','A','test.txt', '\t')
	#inferred_print_line('1.0','2.0','test.txt', '\t')
	#inferred_print_line('1','2','test.txt', '\t')
	#number_lines('1','2','test.txt','roman', '\t')
	#number_lines('i','ii','test.txt','roman', '\t')
	#number_lines('i','ii','test.txt','ROMAN', '\t')
	#number_lines('A','A','test.txt','ALPHA','\t')
	#number_lines('a','a','test.txt','alpha','\t')

	#number_lines('1.0', '2.0','test.txt', 'FLOAT', '\t')
	#number_lines('1', '2','test.txt', 'INTEGER', '\t')


#///////////////////////////////////////////////////////////////////////////////////////////////


	#Base case where only program is called
	if len(argv)<=1:
		return	

	#Case where the help is called
	elif argv[1] == '--help' or argv[1] == '-h':
		print_file_to_screen("helpfile.txt")
		return

	#Case where the version is called
	elif argv[1] == '--version' or argv[1] == '-v':
		print_file_to_screen("versionfile.txt")	
		return

	#Format implementation
	elif argv[1]=='-f' or argv[1]=='--format':
		if len(argv) == 4 and is_argv_number(3):
			build_format_seq("1",argv[3],argv[2],"1")

		elif len(argv) == 5 and is_argv_number(3):
			build_format_seq(argv[3],argv[4],argv[2],1)

		elif len(argv)== 6 and is_argv_number(3):
			build_format_seq(argv[3],argv[5],argv[2],argv[4])

		else:
			error()



	#Format Word implementation
	elif argv[1] == '--format-word' or argv[1]=='-F':
		
		if len(argv) > 6:
			error()
		
		elif argv[2] == 'arabic' and is_argv_equalto('INTEGER') == True:
			if len(argv) == 4:
				build_seq('1',argv[3],'1')
			elif len(argv) == 5:
				build_seq(argv[3], argv[4], '1')
			elif len(argv) == 6:
				build_seq(argv[3], argv[5], argv[4])
			else:
				error()

		elif argv[2] == 'floating' and is_argv_equalto('FLOAT') == True:
			if len(argv) == 4:
				build_seq('1.0',argv[3],'1.0')
			elif len(argv) == 5:
				build_seq(argv[3], argv[4], '1.0')
			elif len(argv) == 6:
				build_seq(argv[3], argv[5], argv[4])
			else:
				error()

		elif argv[2] == 'ALPHA' and is_argv_equalto('ALPHA') == True:
			if len(argv) == 4:
				build_alpha_seq('A',argv[3],'A', True)
			elif len(argv) == 5:
				build_alpha_seq(argv[3], argv[4], 'A', True)
			elif len(argv) == 6:
				build_alpha_seq(argv[3], argv[5], argv[4], True)
			else:
				error()	
		elif argv[2] == 'alpha' and is_argv_equalto('alpha') == True:
			if len(argv) == 4:
				build_alpha_seq('A',argv[3],'A', False)
			elif len(argv) == 5:
				build_alpha_seq(argv[3], argv[4], 'A', False)
			elif len(argv) == 6:
				build_alpha_seq(argv[3], argv[5], argv[4], False)
			else:
				error()	
			
		elif argv[2] == 'ROMAN' and is_argv_int_or_roman(3) == True:
			if len(argv) == 4:
				build_roman_seq('1',argv[3],'1', True)
			elif len(argv) == 5:
				build_roman_seq(argv[3], argv[4], '1', True)
			elif len(argv) == 6:
				build_roman_seq(argv[3], argv[5], argv[4], True)
			else:
				error()
			
		elif argv[2] == 'roman' and is_argv_int_or_roman(3) == True:
			if len(argv) == 4:
				build_roman_seq('1',argv[3],'1', False)
			elif len(argv) == 5:
				build_roman_seq(argv[3], argv[4], '1', False)
			elif len(argv) == 6:
				build_roman_seq(argv[3], argv[5], argv[4], False)
			else:
				error()
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
		build_inferred_seq(argv[1],argv[3],argv[2])
	
	elif len(argv) == 3 and is_argv_number(1):
		build_inferred_seq(argv[1],argv[2],1)

	elif len(argv) == 2 and is_argv_number(1):
		build_inferred_seq(1,argv[1],1)

	#inferred Roman Sequence
	elif len(argv) == 4 and is_argv_int_or_roman(1):
		build_inferred_seq(argv[1],argv[3],argv[2])
	elif len(argv) == 3 and is_argv_int_or_roman(1):
		build_inferred_seq(argv[1],argv[2],1)
	elif len(argv) == 2 and is_argv_int_or_roman(1):
		build_inferred_seq(1,argv[1],1)
	
	#Numberlines inpmlementation
	elif argv[1] == '-n' or argv[1] == '--number-lines':

		if len(argv) <= 2 or len(argv) >= 8:
			error()

		#used to print system arguments for test
		
		# for i in range(1,len(argv)):
		# 	print 'argv['+str(i)+'] '+argv[i]

	
		# print 'number of args ' +str(len(argv))
		

		#Set default
		sepFlag = False
		
		
		#default Separator Character
		sepChar = ' '

		
		if len(argv) > 2:
			if argv[2].startswith('--separator'):
				separator = '--separator'
				sepLen = separator.__len__()
				sepString = argv[2]
				sepChar = sepString[sepLen:]
				sepFlat = True
				#print sepChar

			if argv[2].startswith('-s'):
				separator = '-s'
				sepLen = separator.__len__()
				sepString = argv[2]
				sepChar = sepString[sepLen:]
				sepFlag = True
				#print sepChar

		if len(argv) > 3:
			if argv[3].startswith('--separator'):
				separator = '--separator'
				sepLen = separator.__len__()
				sepString = argv[3]
				sepChar = sepString[sepLen:]
				sepFlat = True
				#print sepChar

			if argv[3].startswith('-s'):
				separator = '-s'
				sepLen = separator.__len__()
				sepString = argv[3]
				sepChar = sepString[sepLen:]
				sepFlag = True
				#print sepChar
		
		#For testing and debugging purposes	
		#print 'Flag ' + str(sepFlag)

		if sepFlag == False:
			try:
				if len(argv) == 3:
					inferred_print_line('1','1', argv[2], sepChar)


				if len(argv) == 4 and argv[2] == 'ROMAN':
					number_lines('1','1',argv[3] ,'ROMAN', sepChar)

				if len(argv) == 4 and argv[2] == 'roman':
					number_lines('1','1',argv[3] ,'roman', sepChar)

				if len(argv) == 4 and argv[2] == 'ALPHA':
					number_lines('A','A',argv[3] ,'ALPHA', sepChar)

				if len(argv) == 4 and argv[2] == 'alpha':
					number_lines('a','a',argv[3] ,'alpha', sepChar)

				if len(argv) == 4 and argv[2] == 'arabic':
					number_lines('1','1',argv[3],'INTEGER', sepChar)	

				if len(argv) == 4 and argv[2] == 'floating':
					number_lines('1.0','1.0',argv[3],'FLOAT', sepChar)		


				if len(argv) == 4:
					increm = increment_by_one(argv[3])
					inferred_print_line(argv[3], increm, argv[2], sepChar)



				if len(argv) == 5 and argv[2] == 'ROMAN':
					number_lines(argv[4],'1',argv[3],'ROMAN', sepChar)

				if len(argv) == 5 and argv[2] == 'roman':
					number_lines(argv[4],'1',argv[3],'roman', sepChar)

				if len(argv) == 5 and argv[2] == 'ALPHA':
					number_lines(argv[4],'A',argv[3] ,'ALPHA', sepChar)

				if len(argv) == 5 and argv[2] == 'alpha':
					number_lines(argv[4],'a',argv[3],'alpha', sepChar)

				if len(argv) == 5 and argv[2] == 'arabic':
					number_lines(argv[4],'1',argv[3],'INTEGER', sepChar)	

				if len(argv) == 5 and argv[2] == 'floating':
					number_lines(argv[4],'1.0',argv[3] ,'FLOAT', sepChar)



				if len(argv) == 5:
					inferred_print_line(argv[3],argv[4] ,argv[2], sepChar)



				if len(argv) == 6 and argv[2] == 'ROMAN':
					number_lines(argv[4], argv[5],argv[3],'ROMAN', sepChar)

				if len(argv) == 6 and argv[2] == 'roman':
					number_lines(argv[4], argv[5],argv[3],'roman', sepChar)

				if len(argv) == 6 and argv[2] == 'ALPHA':
					number_lines(argv[4], argv[5],argv[3],'ALPHA', sepChar)

				if len(argv) == 6 and argv[2] == 'alpha':
					number_lines(argv[4], argv[5],argv[3],'alpha', sepChar)

				if len(argv) == 6 and argv[2] == 'arabic':
					number_lines(argv[4], argv[5],argv[3],'INTEGER', sepChar)	

				if len(argv) == 6 and argv[2] == 'floating':
					number_lines(argv[4], argv[5],argv[3] ,'FLOAT', sepChar)

				if len(argv) == 7:
					error()

				else:
					error()

			except ValueError:
				error()

		
		if sepFlag == True:
			try:
				if len(argv) == 4:
					inferred_print_line('1','1', argv[3], sepChar)

				if len(argv) == 5 and argv[2] == 'ROMAN':
					number_lines('1','1',argv[4],'ROMAN', sepChar)

				if len(argv) == 5 and argv[2] == 'roman':
					number_lines('1','1',argv[4],'roman', sepChar)

				if len(argv) == 5 and argv[2] == 'ALPHA':
					number_lines('A','A',argv[4],'ALPHA', sepChar)

				if len(argv) == 5 and argv[2] == 'alpha':
					number_lines('a','a',argv[4],'alpha', sepChar)

				if len(argv) == 5 and argv[2] == 'arabic':
					number_lines('1','1',argv[4],'INTEGER', sepChar)	

				if len(argv) == 5 and argv[3] == 'floating':
					number_lines('1.0','1.0',argv[4],'FLOAT', sepChar)



				if len(argv) == 5:
					increm = increment_by_one(argv[4])
					inferred_print_line(argv[4], increm, argv[3], sepChar)



				if len(argv) == 6 and argv[2] == 'ROMAN':
					number_lines(argv[5],'1', argv[4],'ROMAN', sepChar)

				if len(argv) == 6 and argv[2] == 'roman':
					number_lines(argv[5],'1', argv[4],'roman', sepChar)

				if len(argv) == 6 and argv[2] == 'ALPHA':
					number_lines(argv[5],'A', argv[4],'ALPHA', sepChar)

				if len(argv) == 6 and argv[2] == 'alpha':
					number_lines(argv[5],'a', argv[4],'alpha', sepChar)

				if len(argv) == 6 and argv[2] == 'arabic':
					number_lines(argv[5],'1', argv[4],'INTEGER', sepChar)	

				if len(argv) == 6 and argv[2] == 'floating':
					number_lines(argv[5], '1.0', argv[4],'FLOAT', sepChar)
					

				if len(argv) == 6:
					inferred_print_line(argv[4],argv[5] ,argv[3], sepChar)


				if len(argv) == 7 and argv[2] == 'ROMAN':
					number_lines(argv[5], argv[6] , argv[4],'ROMAN', sepChar)

				if len(argv) == 7 and argv[2] == 'roman':
					number_lines(argv[5], argv[6] , argv[4],'roman', sepChar)

				if len(argv) == 7 and argv[2] == 'ALPHA':
					number_lines(argv[5], argv[6] , argv[4],'ALPHA', sepChar)

				if len(argv) == 7 and argv[2] == 'alpha':
					number_lines(argv[5], argv[6] , argv[4],'alpha', sepChar)

				if len(argv) == 7 and argv[2] == 'arabic':
					number_lines(argv[5], argv[6] , argv[4],'INTEGER', sepChar)	

				if len(argv) == 7 and argv[2] == 'floating':
					number_lines(argv[5], argv[6] , argv[4],'FLOAT', sepChar)

				else:
					error()

			
			except ValueError:
				error()

		


	else:
		error()




if( __name__ == "__main__" ): 
	main()

#*********************************************************************************************
