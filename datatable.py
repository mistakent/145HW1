# datatable.py; Table editor for terminal
# Alan Salazar Wink - 999868379
# 
# 
# 
# Usage:
# python datatable.py file
# 'file': file to be opened
# User commands:
# 'c': Change an entry.
# 'a': Add a new row/column.
# 'd': Delete a row/column.
# 'u': Undo last change.
# 's': Save file.
# 'q': Quit program.

import sys
import tableFile

def main():
	# Open file
	try:
		tFile = tableFile.tableFile(sys.argv[1])
	except:
		print "Usage:\npython datatable.py <filename>"
		
	# Run editor
	#tEditor = tableEditor(tFile)
	
# Run main
if __name__ == '__main__':
	main()