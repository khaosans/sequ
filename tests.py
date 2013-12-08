#!/usr/bin/python3
#this Python File uses the following encoding: utf-8
#Souriya Khaosanga © 2013
#CS300 Fall Term 2013

#Test Script used for comparing my seq function with GNU seq functions

import os;

def is_sameGNU(toTest):
	print "seq " + toTest
	a = os.popen("python sequ.py "+ toTest)
	b = os.popen("seq "+ toTest)
	testA = a.read()
	testB = b.read()

	if (testA == testB):
		print 'True \n'
		return True
	else:
		print 'False \n'
		return False

def test_case(testCase, expected):
	print "seq " + testCase + " should PASS"
	a = os.popen("python sequ.py "+ testCase)
	b = expected

	testA = a.read()
	testB = b

	print testA

	if (testA == testB):
		print 'True \n'
		return True
	else:
		print 'False \n'
		return False

def expect_fail(testCase, expected):
	print "seq " + testCase + " should FAIL"
	a = os.popen("python sequ.py "+ testCase)
	b = expected

	testA = a.read()
	testB = b

	print testA

	if (testA != testB):
		print 'True \n'
		return True
	else:
		print 'False \n'
		return False

def sysout(testCase):

	print 'python sequ.py '+testCase
	os.system("python sequ.py "+ testCase)
	

if __name__ == '__main__':

	

	
	#Implementation Test for CL 3 
	sysout('i v')
	sysout('1 V x')
	sysout('I v 10')
	sysout('1 2 12.0')
	sysout('1.0 V 45.0')
	sysout('1 vii XX')


	sysout('-F roman xx')
	sysout('--format-word ROMAN XX')
	sysout('-F roman i v xx')
	
	sysout('--format-word alpha a z')
	sysout('-F ALPHA P')
	sysout('-F ALPHA P K')
	sysout('-F ALPHA K P')
	sysout('-F ALPHA A B Z')

	sysout('-F alpha P')
	sysout('-F alpha k')
	sysout('-F alpha p k')
	sysout('-F alpha k p')
	sysout('-F alpha a n z')

	sysout('--format-word ROMAN')
	sysout('--format-word ROMAN XX')
	sysout('-F ROMAN II XXX')
	sysout('-F ROMAN II IV L')
	sysout('-F ROMAN 20')
	sysout('-F ROMAN 1 25')
	sysout('-F ROMAN 1 IV 25')

	sysout('-F roman 12')
	sysout('-F roman 1 xx')
	sysout('-F roman x v l')
	sysout('-F roman 1 iv l')

	sysout('--format-word floating 10.0')
	sysout('-F floating 1.0 5.1')
	sysout('-F floating 1.0 2.2 20.5')

	sysout('--format-word arabic 20')
	sysout('-F arabic 1 9')
	sysout('-F arabic 1 2 12')
	
	# CL 4 Tests
	sysout('-n t2.txt')
	sysout('-n t2.txt i')
	sysout('-n t2.txt I II')
	sysout('-n t2.txt 5 10')
	sysout('--number--lines test.txt clea2.0')
	sysout('-n -s*** t2.txt')
	
	sysout('-n -s** t2.txt')
	sysout('-n -s** t2.txt')
	sysout('-n -s* test.txt 10')
	sysout('-n -s* test.txt 1 ii')  
	sysout('-n -s** test.txt i')
	sysout('-n -s** test.txt I I')
	sysout('-n -s** test.txt 1.0')
	sysout('-n -s** t2.txt i')
	sysout('-n -s** test.txt i ii')

	sysout('-n arabic test.txt')
	sysout('-n arabic t2.txt 10')
	sysout('-n arabic t2.txt 20 5')
	sysout('-n arabic -s** t2.txt')
	sysout('-n arabic -s** t2.txt 5')
	sysout('-n arabic -s** t2.txt 2 6')
	sysout('-n arabic -s** t2.txt 2 5 5') #should fail
	

	sysout('-n floating test.txt')
	sysout('-n floating t2.txt 10.0')
	sysout('-n floating t2.txt 20.0 5.0')
	sysout('-n floating -s** t2.txt')
	sysout('-n floating -s** t2.txt 5.0')
	sysout('-n floating -s** t2.txt 2.1 6.2')
	sysout('-n floating -s** t2.txt 2.0 5.1 5.2') #should fail
	

	sysout('-n ROMAN test.txt')
	sysout('-n ROMAN t2.txt XX')
	sysout('-n ROMAN t2.txt XX V')
	sysout('-n ROMAN -s** t2.txt')
	sysout('-n ROMAN -s** t2.txt VI')
	sysout('-n floating -s** t2.txt V II')
	

	sysout('-n roman test.txt')
	sysout('-n roman t2.txt xx')
	sysout('-n roman t2.txt xx x')
	sysout('-n roman -s** t2.txt')
	sysout('-n roman -s** t2.txt vii')
	sysout('-n roman -s** t2.txt v ix')

	
	sysout('-n ALPHA test.txt')
	sysout('-n ALPHA t2.txt A')
	sysout('-n ALPHA t2.txt C A')
	sysout('-n ALPHA -s** t2.txt')
	sysout('-n ALPHA -s** t2.txt B')
	sysout('-n ALPHA -s** t2.txt B K')

	sysout('-n alpha test.txt')
	sysout('-n alpha t2.txt a')
	sysout('-n alpha t2.txt c a')
	sysout('-n alpha -s** t2.txt')
	sysout('-n alpha -s** t2.txt k')
	sysout('-n alpha -s** t2.txt k k')

	

	


