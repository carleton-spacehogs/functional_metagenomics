for S in $@
do
cd $S
anvi-import-collection -c *external_calls.db -p SAMPLES-MERGED-RNA_v3/PROFILE.db -C ${S}_bins_v232 ~/file_org/MAG_data/bin_collections/${S}*.txt
anvi-summarize -c *external_calls.db -p SAMPLES-MERGED-RNA_v3/PROFILE.db -C ${S}_bins_v232 -o SUMMARY_${S}_bins_RNA
cd ..
done

