#goes through each of my hitcount files and counts the total number of single copy COGs in each metagenome
# this script just tallies all of the hits to any single copy COGs and then divides that total number by 35, since there are 35 single copy COGs
#this script also does not generate an outfile; it just reports numbers.
#usage: normalize_JGI_hitcount_files_fixed.py

import sys, os, numpy, glob
path = r'./'

COGfile = open('list_of_single_copy_cogs.txt','r')
COGlist = []
for l in COGfile:
	cols = l.split('\t')
	COGnum = cols[0]
	COGlist.append(COGnum)
COGfile.close()

for fileName in glob.glob(os.path.join(path, '*calculated_and_annotated_COG.txt')):
	print fileName
	fileName = fileName.lstrip('./')
	infile = open(fileName).read()
	counter = 0
	lines = infile.split('\n')
	for line in lines[:-1]:
		columns = line.split('\t')
		dbnum = columns[1]
		hitcount = float(columns[2])
		if dbnum in COGlist:
			#print dbnum
			counter = counter + hitcount
#	print 'Total number of hits to single-copy COGs:'
#	print counter
	average_hits = float(counter / 35) #this is different; i was doing it wrong before i think: it divides total hits to all of these single copy COGs by 35 (which is number of single-copy COGs)
	#print average_hits
	print 'Average coverage for all 35 single-copy cogs:' 
	print average_hits

