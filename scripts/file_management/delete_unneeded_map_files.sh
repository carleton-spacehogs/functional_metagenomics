for dir in FS844 FS848 FS851 FS852 FS854 FS856 FS866 FS872 FS874 FS877 FS879 FS881
do
cd $dir 
mv -v *.sam ~/file_org/to_delete/
mv -v *_idba.bam ~/file_org/to_delete/
cd ..
done
