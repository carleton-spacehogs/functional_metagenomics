#takes samtools bedcov output and calculates average coverage per ORF and assigns each ORG a pfam number.
#usage: calculate_gene_coverage_annotate_ko.py [output of samtools bedcov] [ko file for that metagenome]

import re
from sets import Set
import sys

bedcovfile = sys.argv[1]
KOfile = sys.argv[2]

#make a dictionary
Ddb ={}
dictfile = open(KOfile, 'r')
for line in dictfile:
	#print line
	columns = line.split('\t')
	seqname = columns[0]
	#print seqname
	database = columns[1].rstrip('\n')
	Ddb[seqname] = database
	#print Ddb
	
#make an outfile
outfile = open(str(bedcovfile.replace('_ORF_coverage.txt', '_ORF_coverage_calculated_and_annotated_pfam.txt')), 'w')
        
#now open the ORF_coverage file and match the seqname and number to the annotation and database.
infile = open(bedcovfile, 'r')
for l in infile:
	cols = l.split('\t')
	sequence = cols[3]
	#print sequence
	start = float(cols[1])
	stop = float(cols[2])
	sum_perbasecov = float(cols[4])
	diff = stop - start
	#print diff
	cov = sum_perbasecov/diff
	
	try:
			outfile.write(str(sequence) + '\t' + str(Ddb[sequence]) + '\t' + str(cov) + '\n')
		#	print "match!"
	except KeyError:
			outfile.write(str(sequence) + '\t' + 'no annotation' + '\t' + str(cov) + '\n')

outfile.close()
infile.close()
dictfile.close()

