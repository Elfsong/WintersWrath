import sys

count = int(sys.argv[1]) 

i = 2

while(count > 0):
	if( (i % 2 == 0) or (i % 3 == 0) ):
		count = count - 1
	i = i + 1
	pass

print(i-1)
print("Done!")
