# This Python File uses the following encoding: utf-8
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

def main(): 

	#Check to see if there are exactly two arguments on 
	if len(sys.argv) == 3:	
		beg = sys.argv[1]
		end = sys.argv[2]
		#Checks for the test cases of input
		#Both numbers are positive
		if beg.isdigit()==True and end.isdigit()==True:
			buildSequence(beg,end)
		#Both numbers are negative
		elif beg.startswith('-')==True and beg[1:].isdigit()==True and end.startswith('-')==True and end[1:].isdigit()==True: 
			buildSequence(beg,end)
		#first number is positive and second number is negative		
		elif beg.isdigit()==True and end.startswith('-')==True and end[1:].isdigit()==True:
			buildSequence(beg,end)
		#first number is negative and second number is positive
		elif beg.startswith('-')==True and beg[1:].isdigit()==True and end.isdigit()==True:
			buildSequence(beg,end)
		else:
			#Status code error
			print 'status code 1'
			return
	
	else:
		#status code error
		print 'status code 1'
		return


if( __name__ == "__main__" ): 
	main()


