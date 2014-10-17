# tableFile.py; Table manager for datatable.py
# Alan Salazar Wink - 999868379
# 
# 
# 

import sys

class tableFile:

	# Constructor: Receives filename
	def __init__(self, filename):
		# Open file
		self.filename = filename
		f = open(filename, 'r')

		# Split data lists of lines with lists of columns
		self.data = map(str.split, f.readlines())
		
		# Close file
		f.close()
		
		# Set the max length element
		self.maxSize = 0;
		self.setMaxSize()
		
	# Return the size of the largest element in the double list
	def setMaxSize(self):
		maxString = []

		# Check if there is the same number of columns in each line
		colNum = len(self.data[0]);

		# Get max of each line
		for i in range(len(self.data)):
			# Wrong number
			if colNum != len(self.data[i]):
				print "Not the same number of columns"
				sys.exit()
			maxString.append(max(self.data[i], key = len))
		
		# Get total max
		self.maxSize = len(max(maxString, key = len));

	# Convert self.data to a single string in the output format
	def listListToString(self):
		return '\n'.join(map(' '.join, self.data))

	# Write table back in the file
	def writeFile(self):
		f = open(self.filename, 'w')
		f.write(self.listListToString())
		f.close();

