#this Python File uses the following encoding: utf-8
#Souriya Khaosang � 2013
#CS300 Fall Term 2013

#sequ Complience Level 0 ***CHECK***TESTED**
#sequ Complience Level 0 ***CHECK***NOT TESTED**
#Requires Basic functionality 

#Library used for system argument 
from sys import argv;


#created an error functio
def error():
	print 'status code 1'
	exit(1)

#Print file to screen
def printFileToScreen(fileToPrint):
	a = open(fileToPrint, "r")
	line = a.readline()
	while line:
		print line
		line = a.readline()
	a.close()


#function is used to print string inputs into integer outputs
#in sequential order
def buildSequence(beg,end,increm):
	#Converts the strings it integers
	begining = convertNum(beg)
	ending = convertNum(end)
	#Prints those numbers
	while begining<=ending:
		print begining
		begining+=increm
	return

def convertNum(number):
	try:
		return int(number)
	except ValueError:
		return float(number)



#function builds the sequence for floating point numbers and pads
#the values with 0
def buildSeqPad(beg, end, increment):
	
	
	begining = convertNum(beg)
	ending = convertNum(end)
	increm = convertNum(increment)
	
	strBeg = str(begining)
	strEnd = str(ending)	
	
	if typeOfValue(beg) == float or typeOfValue(end)==float:
		floatBeg = float(begining)
		floatEnd = float(ending)
		strBeg = str(floatBeg)
		strEnd = str(floatEnd)	
	
	begLength = strBeg.__len__()
	endLength = strEnd.__len__()

	if begLength >= endLength:
		maxLength = begLength
	else:
		maxLength = endLength


	while begining <= ending:
		stringToPrint = str(begining)
		print stringToPrint.zfill(maxLength)	
		begining += increm
		
	return

#Prints the sequence of numbers for floating Point Numbers
def buildFloatSeq(beg,end,increment):
	begining = convertNum(beg)
	ending = convertNum(end)
	increm = convertNum(increment)
	
	while begining <= ending:
		print begining
		begining += increm
	return

#From Stackoverflow how to test with python if str variable contains int float
def typeOfValue(text):
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

#Used for printing the seperator function
def buildSepSeq(beg,end,character,increment):
	begining = convertNum(beg)
	ending = convertNum(end)
	increm = convertNum(increment)
	if begining > ending:
		return
	elif begining == ending:
		print begining
		return
	else:		
		tempString = ''
		while begining<=ending-increm:
			tempString += str(begining)
			tempString += character
			begining += increm
		tempString +=str(begining)
		print tempString
		return

#Used to print the format sequence	
def buildFormatSeq(beg, end, inString, increment):
	begining = convertNum(beg)
	ending = convertNum(end)
	increm = convertNum(increment)

	while begining<=ending:
		print (inString  %  begining)
		begining+=increm
	return
#check for non float and int value and return a boolean value
def isArgvNumber(beginValue):
	lastValue = len(argv)
	for i in range(beginValue,lastValue):
		if typeOfValue(argv[i])==str:
			return False
	return True

			
		
	
	
	

# Main part of the program exist below this point	
def main():

			
	#Case where no arguments exist only the call of the program
	if len(argv)<=1:
		return	
	#Case where the help is called
	if argv[1] == '--help' or argv[1] == '-h':
		printFileToScreen("helpfile.txt")
		return
	#Case where the version is called
	if argv[1] == '--version' or argv[1] == '-v':
		printFileToScreen("versionfile.txt")	
		return

	#Test cases for format
	if argv[1]=='-f' or argv[1]=='--format':
		if len(argv) == 4:
			#arguments of argv beyond index 2 is a float or an int
			if isArgvNumber(3): 
				buildFormatSeq("1",argv[3],argv[2],"1")
			else:
				error()
			
		elif len(argv) == 5: 
			if isArgvNumber(3):
				buildFormatSeq(argv[3],argv[4],argv[2],1)

			else:
				error()
		elif len(argv)== 6:
			if isArgvNumber(3):
				buildFormatSeq(argv[3],argv[5],argv[2],argv[4])
			else:
				error()
		else:
			error()
	#test cases for equal width
	elif argv[1] == '--equal-width' or argv[1]=='-w':
		if len(argv) == 3:
			if isArgvNumber(2):
				buildSeqPad("1",argv[2],"1")
			else:
				error()
			
		if len(argv) ==  4:
			if isArgvNumber(2):
				buildSeqPad(argv[2],argv[3],"1")
			else:
				error()
		if len(argv) == 5:
			if isArgvNumber(2):
				buildSeqPad(argv[2],argv[4],argv[3])
			else:
				error()

	#test cases for separator
	elif argv[1].startswith('--separator'):
		separator = '--separator'
		sepLen = separator.__len__()
		sepString = argv[1]
		sepChar = sepString[sepLen:]
		if len(argv) == 3:
			if isArgvNumber(2):
				buildSepSeq("1",argv[2],sepChar,"1")
			else:
				error()
		if len(argv) == 4:
			if isArgvNumber(2):
				buildSepSeq(argv[2],argv[3],sepChar,"1")
			else:
				error()
		if len(argv) == 5:
			if isArgvNumber(2):
				buildSepSeq(argv[2],argv[4],sepChar,argv[3])
			else:
				error()
	#test cases for -s					
	elif argv[1].startswith('-s'):
		separator = '-s'
		sepLen = separator.__len__()
		sepString = argv[1]
		sepChar = sepString[sepLen:]

		if len(argv) == 3:
			if isArgvNumber(2):
				buildSepSeq("1",argv[2],sepChar,"1")
			else:
				error()
		if len(argv) == 4:
			if isArgvNumber(2):
				buildSepSeq(argv[2],argv[3],sepChar,"1")
			else:
				error()
		if len(argv) == 5:
			if isArgvNumber(2):
				buildSepSeq(argv[2],argv[4],sepChar,argv[3])
			else:
				error()
	#Only integers as system arguments
	elif len(argv) == 4:
		if isArgvNumber(2):
			buildFloatSeq(argv[1],argv[3],argv[2])
		else:
			error()

	#Check to see if there are exactly two arguments on 
	elif len(argv) == 3:	
		#Checks for the test cases of input
		if typeOfValue(argv[1]) == int and typeOfValue(argv[2]) == int:
			buildSequence(argv[1],argv[2],1)
		elif isArgvNumber(2):
			buildFloatSeq(argv[1],argv[2],1)
		else:
			error()
	elif len(argv) == 2:
							
		if isArgvNumber(1):
			buildSequence(1,argv[1],1)
		else:
			error()
	
	else:
		error()


if( __name__ == "__main__" ): 
	main()


