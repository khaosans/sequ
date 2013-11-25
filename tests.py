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

	if (testA != testB):
		print 'True \n'
		return True
	else:
		print 'False \n'
		return False



if __name__ == '__main__':

	print 'Implementation 0 and 1 test information (same as GNU)------------------------- \n'
	is_sameGNU("3 5")
	is_sameGNU("5")
	is_sameGNU("-5 2 10")
	is_sameGNU("-w -5 50 20")
	is_sameGNU("-w -1 .1 1")
	is_sameGNU("-5 10 100")

	print 'Implementation 2 test information--------------------------------------- \n'
	test_case("-W TEST","T E S T\n")
	expect_fail("-W TEST","TEST\n")
	test_case("-W TEST234 TEST4", "T E S T 2 3 4\nT E S T 4\n")
	test_case("--words abc","a b c\n")
	test_case("-P 10"," 1\n 2\n 3\n 4\n 5\n 6\n 7\n 8\n 9\n10\n")
	expect_fail("-P 10","1 2 3 4 5 6 7 8 9 10")
	test_case("-P 0 500 1000","   0\n 500\n1000\n")
	test_case("-P -1000 500 1000","-1000\n -500\n    0\n  500\n 1000\n")
	expect_fail("-P 0","1")
	test_case("--pad-spaces -1000 500 1000","-1000\n -500\n    0\n  500\n 1000\n")
	test_case("--pad-spaces -5 2 1","-5\n-3\n-1\n 1\n")
	test_case("-P -.1 .5 1","-0.1\n 0.4\n 0.9\n")
	test_case("--P","status code 1\n")
	test_case("improper input","status code 1\n")
	test_case("-p '@' 10", "@1\n@2\n@3\n@4\n@5\n@6\n@7\n@8\n@9\n10\n")
	test_case("-p '*' 0 100 300","**0\n100\n200\n300\n")
	test_case("-p improperinput", "status code 1\n")
	test_case("-p '\n' 3", "1\n2\n3\n")
	test_case("--pad '\t' -10 10 20","-10\n\t\t0\n\t10\n\t20\n")
	test_case("--pad ' ' 0 5 10.0", " 0\n 5\n10\n")