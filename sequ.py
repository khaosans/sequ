#This Python File uses the following encoding: utf-8
#Souriya Khaosang © 2013
#CS300 Fall Term 2013

#sequ Complience Level 0
#Requires Basic functionality 

#Library used for system argument 
import sys;

#function is used to print string inputs into integer outputs
#in sequential order
def buildSequence(beg,end):
	#Converts the strings it integers
	begining = convertNum(beg)
	ending = convertNum(end)+1
	#Prints those numbers
	for i in range(begining,ending):
		print i
	return

def convertNum(number):
	try:
		return int(number)
	except ValueError:
		return float(number)

#function builds the sequence of numbers but pads with zero's
#as defined in implementation 1 for integers
def buildSeqPad(beg, end):
	begLength = beg.__len__()
	endLength = end.__len__()

	if begLength >= endLength:
		maxLength = begLength
	else:
		maxLength = endLength

	begining = int(beg)
	ending = int(end)

	for i in range(begining,ending+1):
		stringToPrint = str(i)
		print stringToPrint.zfill(maxLength)
		
	return

#function builds the sequence for floating point numbers and pads
#the values with 0
def buildFloatSeqPad(beg, end):
	begLength = beg.__len__()
	endLength = end.__len__()

	if begLength >= endLength:
		maxLength = begLength
	else:
		maxLength = endLength

	begining = float(beg)
	ending = float(end)

	while begining <= ending:
		stringToPrint = str(begining)
		print stringToPrint.zfill(maxLength)
		begining += 1
		
	return

#Prints the sequence of numbers for floating Point Numbers
def buildFloatSeq(beg,end):
	begining = convertNum(beg)
	ending = convertNum(end)
	
	while begining <= ending:
		print begining
		begining += 1
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

#Used for pritinting the seperator function
def buildSepSeq(beg,end,character):
	begining = convertNum(beg)
	ending = convertNum(end)
	if begining > ending:
		return
	elif begining == ending:
		print begining
		return
	else:		
		tempString = ''
		while begining<=ending-1:
			tempString += str(begining)
			tempString += character
			begining +=1
		tempString +=str(begining)
		print tempString
		return
	
def buildFormatSeq(beg, end, inString, increment):
	begining = convertNum(beg)
	ending = convertNum(end)

	while begining<=ending:
		print (inString  %  begining)
		begining+=increment
	return
	
	

# Main part of the program exist below this point	
def main():
	if sys.argv[1]=='-f' or sys.argv[1]=='--format':
		if len(sys.argv) == 4 and typeOfValue(sys.argv[3])==int or typeOfValue(sys.argv[3])==float:
			buildFormatSeq(1,sys.argv[3],sys.argv[2],1)

		else:
			print 'status code 1'
			return

	elif len(sys.argv) == 4:
		if str(sys.argv[1]) == '--equal-width' or str(sys.argv[1])=='-w': 
			if typeOfValue(sys.argv[2])==float and typeOfValue(sys.argv[3])==float:
				buildFloatSeqPad(sys.argv[2],sys.argv[3])
			elif typeOfValue(sys.argv[2])==int and typeOfValue(sys.argv[3])==int:
				buildSeqPad(sys.argv[2],sys.argv[3])
			elif typeOfValue(sys.argv[2])==float and typeOfValue(sys.argv[3])==int:
				buildFloatSeqPad(sys.argv[2],sys.argv[3])
			elif typeOfValue(sys.argv[2])==int and typeOfValue(sys.argv[3]) == float:
				buildFloatSeqPad(sys.argv[2],sys.argv[3])
			else:
				#status code error
				print 'status code 1'
				return
		elif sys.argv[1].startswith('--separator'):
			separator = '--separator'
			sepLen = separator.__len__()
			sepString = sys.argv[1]
			sepChar = sepString[sepLen:]
			if typeOfValue(sys.argv[2])==float and typeOfValue(sys.argv[3])==float:
				buildSepSeq(sys.argv[2],sys.argv[3],sepChar)
			elif typeOfValue(sys.argv[2])==int and typeOfValue(sys.argv[3])==int:
				buildSepSeq(sys.argv[2],sys.argv[3],sepChar)
			elif typeOfValue(sys.argv[2])==float and typeOfValue(sys.argv[3])==int:
				buildSepSeq(sys.argv[2],sys.argv[3],sepChar)
			elif typeOfValue(sys.argv[2])==int and typeOfValue(sys.argv[3]) == float:
				buildSepSeq(sys.argv[2],sys.argv[3],sepChar)
			else:
				#status code error
				print 'status code 1'
				return
					
		elif sys.argv[1].startswith('-s'):
			separator = '-s'
			sepLen = separator.__len__()
			sepString = sys.argv[1]
			sepChar = sepString[sepLen:]
			if typeOfValue(sys.argv[2])==float and typeOfValue(sys.argv[3])==float:
				buildSepSeq(sys.argv[2],sys.argv[3],sepChar)
			elif typeOfValue(sys.argv[2])==int and typeOfValue(sys.argv[3])==int:
				buildSepSeq(sys.argv[2],sys.argv[3],sepChar)
			elif typeOfValue(sys.argv[2])==float and typeOfValue(sys.argv[3])==int:
				buildSepSeq(sys.argv[2],sys.argv[3],sepChar)
			elif typeOfValue(sys.argv[2])==int and typeOfValue(sys.argv[3]) == float:
				buildSepSeq(sys.argv[2],sys.argv[3],sepChar)
			else:
				#status code error
				print 'status code 1'
				return

		else:
			print 'status code 1'
			return
	#Check to see if there are exactly two arguments on 
	elif len(sys.argv) == 3:	
		beg = sys.argv[1]
		end = sys.argv[2]
		#Checks for the test cases of input
		if typeOfValue(beg) == float and typeOfValue(end) == float :
			buildFloatSeq(beg,end)
		elif typeOfValue(beg) == int and typeOfValue(end) == int:
			buildSequence(beg,end)
		elif typeOfValue(beg) == float and typeOfValue(end) == int:
			buildFloatSeq(beg,end)
		elif typeOfValue(beg) == int and typeOfValue(end)== float:
			buildFloatSeq(beg,end)
		else:
			#Status code error
			print 'status code 1'
			return
	elif len(sys.argv) == 2:
		systemInput = str(sys.argv[1])
		
		if systemInput == '--help' or systemInput == '-h':
			print 'helper'
		elif systemInput == '--version' or systemInput == '-v':
			print 'version'
		else:
			#sttus code error
			print 'status code 1'
			return
	else:
		#status code error
		print 'status code 1'
		return


if( __name__ == "__main__" ): 
	main()


