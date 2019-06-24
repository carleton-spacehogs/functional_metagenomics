#!/usr/bin/env python

# short script to change names from scaffold_# to contig_# in a bed file and write out fixed file
#usage: fix_bed_file.py [name of bed file]

import sys
import os

#read name of bed file
try:
	bed_filehandle = sys.argv[1]
	if "a.bed" not in bed_filehandle:
		raise IOException("Please enter a bed file with the format *.a.bed")
except:
	print("Something went wrong!")

#open the existing bed file
try: 
	bed_file = open(bed_filehandle,'r')
	print("Opening " + bed_filehandle + "...")
except IOError:
	print("Sorry, the file " + bed_file + "was not found.")


# change scaffold to contig names
lines = bed_file.readlines()
bed_file.close()
os.remove(bed_filehandle)
bed_fixed = open(bed_filehandle, 'w')
for line in lines:
	parts = line.split('\t')
	if len(parts) == 1:
		print("Found a blank line after c_" + scaffold_num + ",  moving on...")
		continue
	scaffold_name = parts[0]
	scaffold_name_split = scaffold_name.split("_")
	scaffold_num = int(scaffold_name_split[1]) + 1
	scaffold_num = str(scaffold_num).zfill(12)
	bed_fixed.write("c_" + scaffold_num + '\t' + parts[1] + '\t' + parts[2] + '\t' + parts[3])
	
bed_fixed.close()
print("Bed file closed. Done.")
	
