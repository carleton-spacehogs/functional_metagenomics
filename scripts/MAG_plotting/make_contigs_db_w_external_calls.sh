for S in $@
do
cd $S
anvi-gen-contigs-database -f MidCaymanRise_${S}_idba_assembly_fixed.fa --split-length -1 --external-gene-calls ~/file_org/sample_data/external_gene_calls/${S}_external_gene_calls_matrix.txt --ignore-internal-stop-codons -o ${S}_CONTIGS_external_calls.db
anvi-run-hmms -c *calls.db -T 4
anvi-import-functions -c *calls.db -i ~/file_org/MAG_data/anvio_bin_summary_new/${S}/*functions_matrix.txt
cd ..
done
