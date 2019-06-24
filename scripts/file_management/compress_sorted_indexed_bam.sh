for dir in $@
do
cd $dir
for file in *_sorted.bam
do
tar --remove-files -czvf ${file}.tgz $file
done
for file in *_sorted.bam.bai
do
tar --remove-files -czvf ${file}.tgz $file
done
cd ..
done
