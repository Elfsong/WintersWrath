


import time

def trans( filename ):
	file = open(filename)

	for line in file:
		print( line[:-1] )

if __name__ == "__main__":
	trans("input")
