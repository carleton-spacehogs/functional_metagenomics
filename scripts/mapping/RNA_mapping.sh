#!/bin/bash
# shell script pipeline for doing mapping, sorting, indexing of all reads to all contigs

# Arguments: path to contigs folder, path to reads folder

# for every sample name in the file:
cd $1
pwd
for metagenome in *.fa
do
#make all the index files and put them in the contigs folder
indexedMETA=$(echo $metagenome | cut -d"." -f 1).btindex
echo "bowtie2-build $metagenome $indexedMETA"
bowtie2-build $metagenome $indexedMETA

# mkdir for every sample
metaSAMPLE=$(echo $metagenome | cut -d"_" -f 2)
echo $metaSAMPLE
mkdir ../$metaSAMPLE/
cd ../$metaSAMPLE/
pwd
for reads in ../${2}*.fa
	do
	# get read sample name
	readSAMPLE=$(echo $reads | cut -d"_" -f 4)
	# get file root for this metagenome-read combo
	comboROOT=${readSAMPLE}_RNA_reads_vs_MidCaymanRise_${metaSAMPLE}_idba
	#map
	echo "bowtie2 -x ../${1}${indexedMETA} -f -p 50 -U ../${2}${reads} -S ${comboROOT}.sam"
	bowtie2 -x ../${1}${indexedMETA} -f -p 50 -U ../${2}${reads} -S ${comboROOT}.sam
	#convert to bam
	echo "samtools view -bS ${comboROOT}.sam > ${comboROOT}.bam"
	samtools view -bS ${comboROOT}.sam > ${comboROOT}.bam
	#sort
	echo "samtools sort ${comboROOT}.bam -o ${comboROOT}_sorted.bam" 
	samtools sort ${comboROOT}.bam -o ${comboROOT}_sorted.bam 
	#index
	echo "samtools index ${comboROOT}_sorted.bam"
	samtools index ${comboROOT}_sorted.bam
	done
# cd up 
cd ../$1
pwd
done
