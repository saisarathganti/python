#program searches all the occurance of a file or a directory in entire os
import os , sys

from os.path import join

#converts the commandline argument to string

file1 = ' '.join(sys.argv[1:])

print "f for file d for directory"

word = raw_input()

#takes input to search a file or a directory

key = 0

#key is used to find the occurance of the file

print "searching for %s" % file1

#the fallowing loops searches entire os for the file or the directory needed

for dirs,root,files in os.walk('/'):

	if(word == 'f'):

		if file1 in files:

			print "file exists: %s" % join(dirs,file1)

			key = 1

	elif (word == 'd'):

		if file1 in root:

			print "directory exists: %s" % join(dirs,file1)

			key = 1

	else:
		print "please enter a valid input"

		break
if(key == 0):

	print "No file or directory is found with the given name"


