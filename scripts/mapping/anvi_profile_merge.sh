# given a bunch of sorted/indexed BAM files from a sample AND an anvio contigs DB, make an anvio profile (contigs db) for each of them and then merge the profile into one

# list of args is each folder where your bam files are

#for each directory/location where your bam files are
for sample in $@
do
#cd into the directory
cd $sample
pwd
#for each bam profile
sample=$(echo $sample | cut -d"/" -f 1)
for BAMFile in *sorted.bam
do
# make an anvio profile for each
echo "anvi-profile -i $BAMFile -c CONTIGS.db -T 55" 
anvi-profile -i $BAMFile -c *calls.db -T 55
done
# make a merged profile out of all of your profiles
echo "anvi-merge */PROFILE.db -o SAMPLES-MERGED-RNA_v3 -c CONTIGS.db --skip-concoct-binning"
anvi-merge */PROFILE.db -o SAMPLES-MERGED-RNA_v3 -c *calls.db --skip-concoct-binning
#cd up
cd ..
done
