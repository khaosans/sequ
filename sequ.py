#Souriya Khaosanga
#CS300 

#sequ Complience Level 0


import sys;

def main(): 

	#Check to see if there are exactly two arguments on 
	#command line	
	if len(sys.argv) == 3:	
		beg = sys.argv[1]
		end = sys.argv[2]
		#Check to see if the user input are integers
		if beg.isdigit()==True and end.isdigit()==True:
			begining = int(sys.argv[1])
			ending = int(sys.argv[2])+1 
			#Print incremental sequence of those values
			for i in range(begining, ending):
				print i
		else:
			#Status code error
			print 'status code 1'
			return	
	
	else:
		#status code error
		print 'status code 1'
		return


if( __name__ == "__main__" ): 
	main();

