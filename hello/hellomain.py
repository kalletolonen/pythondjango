#!/usr/bin/python3

import sys

def hello():
	if len(sys.argv) == 2:
		name = sys.argv[1]
		print (f"Hello, {name}")
	elif len(sys.argv) <= 1:
		print ("Hello, noname")
	elif len(sys.argv) > 2:
		for names in sys.argv:
			if "hellomain.py" in names:
				print("So many names!")
			else:
				print (f"Hello: {names}" )

def main():
	hello()

main()

if __name__ == "__main":
	main()
