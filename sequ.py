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
	begining = int(beg)
	ending = int(end)+1
	#Prints those numbers
	for i in range(begining,ending):
		print i
	return

#function builds the sequence of numbers but pads with zero's
#as defined in implementation 1
def buildSequencePad(beg, end):
	begLength = beg.__len__()
	endLength = end.__len__()

	if begLength >= endLength:
		maxLength = begLength
	else:
		maxLength = endLength
	
	begining = int(beg)
	ending = int(end)+1

	for i in range(begining,ending):
		stringToPrint = str(i)
		print stringToPrint.rjust(maxLength,'0')
		
	return

def buildFloatSeq(beg,end):
	begining = float(beg)
	ending = float(end)
	
	while begining <= ending:
		print begining
		begining += 1
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
	
def main():
	 

	#Check to see if there are exactly two arguments on 
	if len(sys.argv) == 3:	
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


