import os

def dirList(curDir):
	fileList = os.listdir(curDir)
	local = len(fileList)
	total = local 
	for i in fileList:
		fullPath = os.path.join(curDir, i)
		if os.path.isdir(fullPath):
			total += dirList(fullPath)
	print('directory: %s local: %s total: %s' % (curDir, local, total))
	return total 

