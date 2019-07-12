#!/usr/bin/env python

import sys, os, glob
path = r'./'

# open text file to write results
def openOutfile(name):
	try:
		outFile = open(name, 'w')
		print "Creating new file '{}'...".format(name)
	except IOError:
		if 'y' or 'Y' in raw_input("'{}' already exists. Do you want to overwrite? y/n... ".format(name)):
			outFile = open(name, 'w')
			print "Opened and overwrote existing file '{}'".format(name)
		else:
			print "Exiting script..."
			sys.exit(0)
	return outFile

#make a dictionary connecting FS name to "real" name
def get_sample_names(name):
	D_sample_names = {}
	# this tab-delimited text file has matches of FS to sample name
	sample_names = open(name, 'r')
	lines = sample_names.readlines()
	sample_names.close()
	# read it in and return the dictionary
	for line in lines:
		cols = line.split('\t')
		D_sample_names[cols[0]] = cols[1].rstrip('\n')
	return D_sample_names
	

def searchSumSU(targetGene, fileLines):
	#function takes gene and inFile lines as arguments
		#part of function # for line in lines (of inFile)
			# See if gene is a subunit of target gene
			# if yes, sum the coverages
		# return the gene, covg and metabolism
	sumCov = 0.0
	subU = ''
	rest = ''
	for line in fileLines:
		cols = line.split('\t')
		gene = cols[1]
		if targetGene in gene[:len(targetGene)]:
			# trying to get rid of space at end of "Sulfur oxidation"
			metabolism = cols[3].rstrip()
			covg = cols[5].rstrip('\n')
			if covg == 'nan':
				covg = 0.0
			sumCov += float(covg)
			subU += gene[len(targetGene):len(targetGene)+1]
			rest += gene[len(targetGene)+1:]
	
	# if the target gene was given as generic three letters, add all the relevant subunit letters to the end of it
	targetGene+=subU
	targetGene+=rest
	try:
		return targetGene, metabolism, sumCov
	except UnboundLocalError, e:
		print "ERROR: " + str(e)
		print "The gene '{}' you listed in 'genes_of_interest*.txt' was likely\nNOT FOUND in the annotated/normalized text file.\nExiting script...".format(targetGene)
		sys.exit(0)
	except Error, e:
		print "ERROR: " + str(e)
		print "Something went wrong. Exiting script..."
		sys.exit(1)


# make a color dictionary connecting metabolism to a color
D_colors = {'hydrogen': 'c', 'Sulfur oxidation': 'y', 'Sulfur reduction (oxidation?)':'y', 
'Methanogenesis':'m', 'Nitrate reduction (denitrification)':'g', 'Nitrogen fixation':'g', 
'Denitrification':'g', 'DNRA':'g', 'Ammonia oxidation/methane oxidation':'m', 'O2 respiration':'b',
'methanol':'k', 'methanol':'m', 'carbon monoxide':'k', 'carbon fixation':'k', 'iron':'r'}

# dict to distinguish VD and PD
L_sites_PD = ['FS851', 'FS852','FS854', 'FS856']

outFile = openOutfile('excel_prep_bins_all_genes.txt')
D_sample_names = get_sample_names('sample_names.txt')

# From Rika's code
# for loop that keeps finding relevant files
print "Files found:"
for fileName in glob.glob(os.path.join(path, '*normalized_KO.txt')):
	#Print the filename
	print fileName
	#write metagenome name to outfile
	fileName = fileName.lstrip('./')
	RNA = False
	if 'RNA' in fileName:
		print 'RNA'
		RNA = True
	metagenome_name = fileName.split('_reads_vs_')[0]
	metagenome_name = metagenome_name.rstrip('_RNA')[7:]
	#D_files[metagenome_name] = fileName
	inFile = open(fileName, 'r')
	lines = inFile.readlines()[1:]
	inFile.close()
	
	genes = open('genes_of_interest_KO.txt', 'r')
	geneLines = genes.readlines()
	genes.close()
	
	if metagenome_name in L_sites_PD:
		site = 'P'
	else:
		site = 'V'	

	gene_num = 1
	for gene in geneLines:
		gene, metabolism, covg = searchSumSU(gene.rstrip(), lines)
		# write gene (variable in for), covg and metabolism to outfile
		outFile.write(str(gene_num) + '\t' +str(covg)+'\t'+ D_sample_names[metagenome_name]+'\t'+gene+'\t'+ metabolism +'\t' + D_colors[metabolism]+'\t' + str(covg*100)+'\t'+str(RNA)+'\t'+site+'\n')
		# 'y-axis' (gene) numbers
		gene_num+=1


for fileName in glob.glob(os.path.join(path, '*normalized_pfam.txt')):
	print fileName
	fileName = fileName.lstrip('./')
	RNA = False
	if 'RNA' in fileName:
		print 'RNA'
		RNA = True
	metagenome_name = fileName.split('_reads_vs_')[0]
	metagenome_name = metagenome_name.rstrip('_RNA')[7:]
	inFile = open(fileName, 'r')
	lines = inFile.readlines()[1:]
	inFile.close()
	
	# for gene in gene in file
	genes = open('genes_of_interest_pfam.txt', 'r')
	geneLines = genes.readlines()
	genes.close()

	if metagenome_name in L_sites_PD:
		site = 'P'
	else:
		site = 'V'
	
	gene_num_2 = gene_num
	for gene in geneLines:
		gene, metabolism, covg = searchSumSU(gene.rstrip(), lines)
		# write gene (variable in for), covg and metabolism to outfile
		outFile.write(str(gene_num_2)+'\t'+str(covg) +'\t'+ D_sample_names[metagenome_name]+'\t'+gene+'\t'+ metabolism +'\t' + D_colors[metabolism]+'\t' + str(covg*100)+'\t'+str(RNA)+'\t'+site+'\n')
		# 'y-axis' (gene) numbers
		gene_num_2+=1
		

outFile.close()
print 'Done.'	
