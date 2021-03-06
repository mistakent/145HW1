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

import sys, traceback, curses
import tableFile, TableEditor, TableDisplayer

#restores terminal screen on any exception below
def restorescreen():
	try:
		curses.nocbreak()
		curses.echo()
		curses.endwin()
	except:
		return

def main():
	# Open file
	try:
		tFile = tableFile.tableFile(sys.argv[1])
	except:
		print "Usage:\npython datatable.py <filename>"
		return

	# Run editor
	try:
		tDisplayer = TableDisplayer.TableDisplayer(tFile)
		tEditor = TableEditor.TableEditor(tFile, tDisplayer)
		tEditor.run()
	except:
		restorescreen()
		traceback.print_exc()
		return
	
# Run main
if __name__ == '__main__':
	main()