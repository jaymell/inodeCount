#!/usr/bin/python

import os

def dirList(curDir):
	""" recursively return total 
		# of inodes in curDir """

	fileList = os.listdir(curDir)
	local = len(fileList)
	total = local 
	for i in fileList:
		fullPath = os.path.join(curDir, i)
		if os.path.isdir(fullPath):
			total += dirList(fullPath)
	#print('directory: %s local: %s total: %s' % (curDir, local, total))
	return total 

def dirListDict(curDir):
	""" recursively return a dict
		that mirrors curDir's tree, and
		total # of inodes in curDir  --"""

	theDict = {}
	fileList = os.listdir(curDir)
	local = len(fileList)
	theDict['local'] = local
	total = local 
	for i in fileList:
		fullPath = os.path.join(curDir, i)
		if os.path.isdir(fullPath):
			theDict[i], runningTotal = dirListDict(fullPath)
			total += runningTotal
	theDict['total'] = total
	return (theDict, total)

if __name__ == '__main__':
	
	import sys
	import pprint

	if len(sys.argv) == 2:
		total1 = dirList(sys.argv[1])
		theDict, total2 = dirListDict(sys.argv[1])
		#pprint.pprint(theDict)
		print("dirList: %d" % int(total1+1))
		print("dirListDict: %d" % int(total2+1))
