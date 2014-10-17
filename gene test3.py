import sys, os, curses

def main():

	words = []
	size = []

	#open file
	f = open(sys.argv[1])

	#put items in an array
	flines = f.readlines()
	linecount = len(flines)
	for l in flines:
		words.append(l.split())

	#test format within terminal (wihtout curses)
	wordcount=0
	#widths = [max(map(len,col)) for col in zip(*words)]
	for row in words:
		wordcount += len(words[1])
	#	print " ".join((val.rjust(width) for val, width in zip(row, widths)))

	#get max length in cols and put in array size
	maxcols = zip(*words)
	for q in range (len(maxcols)):
		size.append(max(maxcols[q], key=len))
	
	#start curses
	s = curses.initscr()

	#displays table
	for l in range (len(flines)):
		for w in range (wordcount/len(flines)):
			s.addstr(words[l][w].rjust(len(size[w]))+' ')
		s.addstr('\n')

	#prints table
	s.refresh()
	sys.stdin.read(1)
	curses.endwin()

if __name__ == '__main__':
	main()
